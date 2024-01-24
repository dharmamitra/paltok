# 0. Overview

At present this repo contains 4 things:

1. scripts for transforming the json formatted text from https://github.com/BuddhaNexus/segmented-pali into tsv-format

2. scripts for preparation of one huge txt-document for training sentencepiece model

3. scripts for running the SPM training

4. scripts for running the FastText training

## Prerequisits

- installed SPM

- built FastText executable

# 1. JSON to TSV

It seems there are 783993 lines in the corpus

`src/pali_json2tsv.py`

# 2. Cleaning text for training (TSV to TXT)

For exploring the text: `src/pali_exploration.py`

Actual job is done by: `src/pali_prep_spm.py`

# 3. Sentencepiece training =TOKENIZATION

`time spm_train --input=pali_for_sentencepiece.txt --model_prefix=pali_spm --vocab_size=4000 --character_coverage=1.0`

`time cat pali_for_sentencepiece.txt | spm_encode --model=pali_spm.model > pali_tokenized_for_fasttext.txt`

# 3. FastText training =VECTORS

[Documentation](https://fasttext.cc/docs/en/unsupervised-tutorial.html)

> In practice, we observe that skipgram models works better with subword information than cbow. 

Build fastText and call from the directory with the fasttext binary:

`time ./fasttext skipgram -input ../paltok/pali_tokenized_for_fasttext.txt -output ../paltok/pali_fasttext.model`

# 4. Results

## Artifacts

1. (zipped) tsv texts

2. sentencepiece model + vocab

3. fasttext model

## Naming, Versioning, Storange

todo

### structure of the proj

## Packaging

the most reusable items seem to be:

1. pali_cleaner function

2. FastText tokenization