import re
import os
from datetime import datetime
from pathlib import Path

TIMESTAMP_SEP = "_"
TIME_FORMAT = "%Y-%m-%d-%H%M"
TIME_PATTERN = "[0-9]{12}"

def stamp2datetime(path: str) -> datetime:
    stem = Path(path).stem
    return datetime.strptime(stem.split(TIMESTAMP_SEP)[-1], TIME_FORMAT)

def get_timestapm(dt: datetime) -> str:
    def dt2str(dt):
        return dt.strftime(TIMESTAMP_SEP + TIME_FORMAT)
    if not dt:
        return dt2str(datetime.now())
    else:
        return dt2str(dt)

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
    # print(path)
    # print(pattern)
    # print(target_paths)
    dates = [stamp2datetime(p) for p in target_paths]
    latest_idx = dates.index(max(dates))
    # print(latest_idx)
    return target_paths[latest_idx]