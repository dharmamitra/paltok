`time spm_train --input=pali_for_sentencepiece.txt --model_prefix=pali_spm --vocab_size=4000 --character_coverage=1.0`


`time cat pali_for_sentencepiece.txt | spm_encode --model=pali_spm.model > pali_tokenized_for_fasttext.txt`

# FastText

[Documentation](https://fasttext.cc/docs/en/unsupervised-tutorial.html)

> In practice, we observe that skipgram models works better with subword information than cbow. 

Build fastText and call from the directory with the fasttext binary:

`time ./fasttext skipgram -input ../paltok/pali_tokenized_for_fasttext.txt -output ../paltok/pali_fasttext.model`
