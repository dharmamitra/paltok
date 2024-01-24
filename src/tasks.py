from invoke import task
from pali_json2tsv import pali_repo2tsv
from pali_prep_spm import pali_prep_spm
import os
from pathlib import Path
from tqdm import tqdm
from timestamp import stamp2datetime, get_timestapm, find_latest
from pali_prep_spm import PALI_FOR_SPM_FILENAME
import sentencepiece as spm

# invoke create-pali-all-tsv --json-dir "../segmented-pali/inputfiles/" --tsv-dir "../pali_all"
@task
def create_pali_all_tsv(c,
        json_dir,
        tsv_dir,
        extention="tsv",
        clone=False,
        archive=False,):
    print("Start processing pali...")

    pali_repo2tsv(
        json_dir=json_dir,
        tsv_dir=tsv_dir,
        extention=extention,
        clone=clone,
        archive=archive,
    )
    return 0

# invoke prep-spm --src-dir="../"
@task
def prep_spm(c, 
            src_dir,
            dest_dir=None,
            debug=False,
            feedback=False,
            ):
    
    pali_prep_spm(
        src_dir = src_dir,
        dest_dir = dest_dir,
        in_extention="tsv",
        archive=False,
        sep="\t",
        DEBUG=debug,
        FEEDBACK=feedback,
    )
    return 0

@task
def print_timestapm(c, path):
    print(get_timestapm(stamp2datetime(path)))
    return 0

@task
def print_txt_for_spm(c, path):
    print(find_latest(path, PALI_FOR_SPM_FILENAME))
    return 0

@task
def train_spm(c, input, model_prefix, vocab_size=4000):
    spm.SentencePieceTrainer.train(input=input, 
                                    model_prefix=model_prefix, 
                                    vocab_size=vocab_size, 
                                    user_defined_symbols=['foo', 'bar'])
    
@task
def encode_for_fasttext(c, input_path, model_path, output_path):
    sp = spm.SentencePieceProcessor()
    sp.load(model_path)
    with open(input_path, "r") as in_file:
        with open(output_path, "w+") as out_file:
            for line in tqdm(in_file):
                tokens = sp.encode_as_pieces(line)
                out_file.write(" ".join(tokens) + "\n")
