import os
import re
from pathlib import Path

import pandas as pd
import shutil

src_dir = Path("/home/wo/bn/paltok/pali_csv/")
dest_file = Path("/home/wo/bn/paltok/pali_for_sentencepiece.txt")

def clean_pali(string):
        string = string.lower()
        string = re.sub(r'[0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\']',"", string) # ascii digits and punctuation
        string = re.sub(r'[\t\n\r\x0b\x0c]'," ", string) # whitespaces apart from " "
        string = re.sub(r'[ṅṁ]',"ṃ", string) # whitespaces apart from " "
        string = re.sub(r'[”ऐạै–…‘“’\\ौऋ—औ]',"ṃ", string)
        return string

with open(dest_file, 'w+') as outputfile:
    for file_path in Path(src_dir).rglob("*.csv"):

        with open(file_path, encoding="utf-8") as inputfile:
            text_col = pd.read_csv(inputfile, header=None)[1]
        for line in text_col:
            line = clean_pali(str(line))
            outputfile.write(line + '\n')

shutil.make_archive("pali_for_sentencepiece", "zip", dest_file, dest_file)

# 783993