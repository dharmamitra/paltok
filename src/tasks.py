from invoke import task
from pali_json2tsv import pali_repo2tsv
import datetime

tsv_dir = "../pali_all"
txt_dir = "../"

@task
def create_pali_all_tsv(c):
    stamp = datetime.datetime.now().strftime('_%Y%m%d%H%M')
    pali_repo2tsv(
        json_dir="../segmented-pali/inputfiles/",
        tsv_dir=tsv_dir + stamp,
        extention="tsv",
        clone=False,
        archive=False,
    )
    return 0

@task
def create_txt_for_spm(c, in_dir=tsv_dir, out_dir=""):
    pass