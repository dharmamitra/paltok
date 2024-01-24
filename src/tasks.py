from invoke import task
from pali_json2tsv import pali_repo2tsv
from pali_prep_spm import pali_prep_spm
from datetime import datetime
import os
import re

TIMESTAMP_SEP = "_"
TIME_FORMAT = "%Y%m%d%H%M"
TIME_PATTERN = "[0-9]{12}$"

def stamp2datetime(path: str) -> str:
    return datetime.strptime(path.split(TIMESTAMP_SEP)[-1], TIME_FORMAT)

def get_timestapm() -> str:
    return datetime.now().strftime(TIMESTAMP_SEP + TIME_FORMAT)

def find_latest(path: str, prefix: str) -> str:
    """in the input dir find the upper level file/dir with the latest timestamp

    Args:
        dir (str): _description_
        prefix (str): without the timestamp separator

    Returns:
        str: _description_
    """
    pattern = prefix + TIMESTAMP_SEP + TIME_PATTERN
    target_paths = [p for p in os.listdir(path) if re.match(pattern, os.path.basename(p))]
    dates = [stamp2datetime(p) for p in target_paths]
    latest_idx = dates.index(max(dates))
    return target_paths[latest_idx]

PALI_TSV_DIR_PREFIX = "pali_all"
PALI_FOR_SPM_FILENAME = "pali_for_spm"

# invoke create-pali-all-tsv --json_dir="" --tsv_dir=""
@task
def create_pali_all_tsv(c,
        json_dir,
        tsv_dir,
        extention="tsv",
        clone=False,
        archive=False,):
    print("start processing pali...")
    stamp = get_timestapm()
    pali_repo2tsv(
        json_dir=json_dir,
        tsv_dir=tsv_dir + stamp,
        extention=extention,
        clone=clone,
        archive=archive,
    )
    return 0

# invoke create-txt-for-spm --src_dir="../"
@task
def prep_spm(c, 
                       src_dir,
                       dest_dir=None,
                       prefix=PALI_TSV_DIR_PREFIX,
                       debug=False,
                       feedback=False,
                       ):
    if not dest_dir:
        dest_dir = src_dir
    print(dest_dir)
    src_dir = src_dir + find_latest(path=src_dir, prefix=prefix)
    feedback_stamp = "" if not feedback else "_feedback"
    dest_file = dest_dir + \
                PALI_FOR_SPM_FILENAME + \
                feedback_stamp + \
                get_timestapm() + \
                ".txt"
    
    pali_prep_spm(
        src_dir = src_dir,
        dest_file = dest_file,
        in_extention="tsv",
        archive=False,
        sep="\t",
        DEBUG=debug,
        FEEDBACK=feedback,
    )
    print("Created ", dest_file)
    pass