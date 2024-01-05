import os
from pathlib import Path

import pandas as pd
import shutil
import re

dest_file = Path("/home/wo/bn/paltok/pali_findings.txt")

def clean_pali(string):
        string = string.lower()
        string = re.sub(r'[0-9!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\']',"", string) # ascii digits and punctuation
        string = re.sub(r'[\t\n\r\x0b\x0c]'," ", string) # whitespaces apart from " "
        string = re.sub(r'[ṅṁ]',"ṃ", string) # whitespaces apart from " "
        # line = line.replace("ạ", "a") # only one case in Pali
        string = re.sub(r'[”ऐạै–…‘“’\\ौऋ—औ]',"ṃ", string)
        return string

collection = set()
allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ " + \
        "āīūṛṝḷḹṅñṭḍṇśṣṃḥ" # + "ĀĪŪṚḶṄÑṬḌṆŚṢ" + "ēō" "ḻṟṉḵṯ"
with open("pali_for_sentencepiece.txt", encoding="utf-8") as inputfile:
    for line in inputfile:
        # line = str(line)
        line = clean_pali(line)
        findings = [sym for sym in line if sym not in allowed]
        collection = set.union(collection, set(findings))


print(len(collection))
print(collection)

with open("findings.txt", "w+") as f:
        f.write("".join(list(collection)))

# print("ĀĪŪṚḶṄÑṬḌṆŚṢ".lower())

# shutil.make_archive("pali_for_sentencepiece", "zip", dest_file, dest_file)

# 783993