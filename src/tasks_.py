from invoke import task
from pali_json2tsv import pali_repo2tsv
tsv_dir = "../pali_all_tsv/"
txt_dir = "../"

@task
def create_pali_all_tsv(c, out_dir=tsv_dir):
    pali_repo2tsv(
        tsv_dir=out_dir
    )
    return 0

@task
def create_txt_for_spm(c, in_dir=tsv_dir, out_dir=""):
    pass