import os
from pathlib import Path

import pandas as pd
import shutil
from tqdm import tqdm

from pali_cleaner import pali_cleaner

def pali_prep_spm(
        src_dir = "../pali_tsv",
        dest_file = "../pali_for_spm.txt",
        in_extention="tsv",
        archive=False,
        sep="\t",
        DEBUG=False,
        FEEDBACK=False,
    ):

    with open(dest_file, 'w+') as outputfile:
        all_paths = Path(src_dir).rglob(f"*.{in_extention}")
        for file_path in tqdm(list(all_paths)):

            with open(file_path, encoding="utf-8") as inputfile:
                df = pd.read_csv(inputfile, sep=sep, header=None)
                segment_ids = df[0]
                text_col = df[1]
            for seg_id, line in zip(segment_ids, text_col):
                cleaned_line = pali_cleaner(str(line))
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
