import os
from pathlib import Path

import pandas as pd
import shutil

from pali_cleaner import pali_cleaner

src_dir = Path("/home/wo/bn/paltok/pali_csv/")
dest_file = Path("/home/wo/bn/paltok/pali_for_sentencepiece.txt")


with open(dest_file, 'w+') as outputfile:
    for file_path in Path(src_dir).rglob("*.csv"):

        with open(file_path, encoding="utf-8") as inputfile:
            text_col = pd.read_csv(inputfile, header=None)[1]
        for line in text_col:
            line = pali_cleaner(str(line))
            outputfile.write(line + '\n')

shutil.make_archive("pali_for_sentencepiece", "zip", dest_file, dest_file)

# 783993