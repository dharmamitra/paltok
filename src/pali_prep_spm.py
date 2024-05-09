import os
from pathlib import Path

import pandas as pd
import shutil
from tqdm import tqdm

from pali_cleaner import clean_pali
from timestamp import get_timestapm, find_latest, stamp2datetime
from pali_json2tsv import PALI_TSV_DIR_PREFIX
PALI_FOR_SPM_FILENAME = "pali_for_spm"

def pali_prep_spm(
        src_dir = "../",
        dest_dir = None,
        in_extention="tsv",
        archive=False,
        sep="\t",
        DEBUG=False,
        FEEDBACK=False,
    ):
    feedback_stamp = "" if not FEEDBACK else "_feedback"
    if not dest_dir:
        dest_dir = src_dir
    src_dir = Path(src_dir) / find_latest(path=src_dir, prefix=PALI_TSV_DIR_PREFIX)
    dest_file = Path(dest_dir) / ( \
                PALI_FOR_SPM_FILENAME + \
                feedback_stamp + \
                get_timestapm(stamp2datetime(str(src_dir))) + \
                ".txt"
                )

    with open(dest_file, 'w+') as outputfile:
        all_paths = Path(src_dir).rglob(f"*.{in_extention}")
        print(">>>", src_dir)
        for file_path in tqdm(list(all_paths)):

            with open(file_path, encoding="utf-8") as inputfile:
                df = pd.read_csv(inputfile, sep=sep, header=None)
                segment_ids = df[0]
                text_col = df[1]
            for seg_id, line in zip(segment_ids, text_col):
                cleaned_line = clean_pali(str(line))
                if DEBUG:
                    if not len(cleaned_line.strip()):
                        print(f"{seg_id} : {line} : ${cleaned_line}$ = {len(cleaned_line)}")
                if FEEDBACK:
                    cleaned_line =f"{seg_id}\t{line}\t${cleaned_line}$ = {len(cleaned_line)}"
                outputfile.write(cleaned_line + '\n')
    if archive:
        shutil.make_archive(
            "pali_for_spm", 
            "zip", 
            dest_file, dest_file # this repetition allows to process a single file
        )

if __name__ == "__main__":
    pali_prep_spm()
