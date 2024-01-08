import os
from pathlib import Path

import pandas as pd
import shutil

src_dir = Path("/home/wo/bn/paltok/segmented-pali/inputfiles/")
dest_dir = Path("/home/wo/bn/paltok/pali_csv/")

def get_new_filename(file_path: os.PathLike, extention: str = "csv") -> str:
    key = "-".join(file_path.parent.parts)
    name = file_path.stem
    return key + "--" + name + "." + extention

for file_path in Path(src_dir).rglob("*.json"):
    new_name = get_new_filename(file_path.relative_to(src_dir))

    with open(file_path, encoding="utf-8") as inputfile:
        df = pd.read_json(inputfile, orient="index")

    dest_dir.mkdir(exist_ok=True)

    df.to_csv(dest_dir / new_name, encoding="utf-8", index=True, header=False)

shutil.make_archive("pali_csv", "zip", dest_dir)
