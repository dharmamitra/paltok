import os
from pathlib import Path

import pandas as pd
import shutil
from git import Repo  # pip install gitpython
from tqdm import tqdm
from timestamp import get_timestapm

PALI_TSV_DIR_PREFIX = "pali_all"

def get_new_filename(file_path: Path, extention: str = "tsv") -> str:
    """create new name by encoding the info about the directory structure 
    by adding the all path's dirs separeted by "-" fron each other 
    and by "--" from the file name. In file name dots are replased by "-"

    Args:
        file_path (Path): _description_
        extention (str, optional): _description_. Defaults to "csv".

    Returns:
        str: _description_
    """
    key = "-".join(file_path.parent.parts)
    name = file_path.stem.replace(".", "_")
    return key + "__" + name + "." + extention


def clone_repo():
    print("Downloading repo")
    Repo.clone_from(url="https://github.com/BuddhaNexus/segmented-pali", 
                    to_path="../segmented-pali")


def pali_repo2tsv(
    json_dir="../segmented-pali/inputfiles/",
    tsv_dir="../",
    extention="tsv",
    clone=True,
    archive=True,
    ):
    if clone:
        clone_repo()
    stamp = get_timestapm(None)

    tsv_dir = Path(tsv_dir + PALI_TSV_DIR_PREFIX + stamp)
    tsv_dir.mkdir(exist_ok=True)

    print("Transforming to TSV")
    all_files = list(Path(json_dir).rglob("*.json"))
    # print(all_files)
    for file_path in tqdm(all_files):
        new_filename = get_new_filename(
            file_path.relative_to(json_dir),
            extention)

        with open(file_path, encoding="utf-8") as inputfile:
            df = pd.read_json(inputfile, orient="index")

        df.to_csv(tsv_dir / new_filename, 
                sep="\t", 
                encoding="utf-8", 
                index=True, header=False)

    if archive:
        print("Zipping")
        shutil.make_archive("../pali_all_tsv", "zip", tsv_dir)

if __name__ == "__main__":
    pali_repo2tsv(archive=True, clone=False)
