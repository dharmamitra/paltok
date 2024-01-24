from invoke import task
from pali_json2tsv import pali_repo2tsv
import datetime
import os

def find_latest(dir: str, prefix: str):
    print(prefix)
    target_paths = [p for p in os.listdir(dir) if os.path.basename(p).startswith(prefix)]
    print(target_paths)

@task
def create_pali_all_tsv(c,
        json_dir,
        tsv_dir,
        extention="tsv",
        clone=False,
        archive=False,):
    print("start processing pali...")
    stamp = datetime.datetime.now().strftime('_%Y%m%d%H%M')
    pali_repo2tsv(
        json_dir=json_dir,
        tsv_dir=tsv_dir + stamp,
        extention=extention,
        clone=clone,
        archive=archive,
    )
    return 0

@task
def create_txt_for_spm(c, dir, prefix):
    find_latest(dir=dir, prefix=prefix)
    pass