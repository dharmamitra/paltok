WORK_DIR=$(pwd)
JSON_DIR=$(realpath ${WORK_DIR}/../segmented-pali/inputfiles/)
OUTPUT_DIR=$(realpath ${WORK_DIR}/../output) #"/output/"
TASKS=$(realpath ${OUTPUT_DIR}/src)
SRC_DIR=${OUTPUT_DIR}/src

FASTTEXT_BINARY=${WORK_DIR}/../fastText/fasttext

mkdir -p ${OUTPUT_DIR}

invoke create-pali-all-tsv \
    --json-dir ${JSON_DIR} \
    --tsv-dir ${OUTPUT_DIR} && \
invoke prep-spm --src-dir=${OUTPUT_DIR}

# the result of the previous step is previous step is found by the latest timestamp

TXT_FOR_SPM=$1
if [ -z ${TXT_FOR_SPM} ]; then
    TXT_FOR_SPM=$(invoke print-txt-for-spm ${OUTPUT_DIR})
fi
SUFFIX=$(invoke print-timestapm --path ${TXT_FOR_SPM})

TOKENIZED=${OUTPUT_DIR}/pali_tokenized_for_fasttext${SUFFIX}.txt

# time spm_train --input=${OUTPUT_DIR}/${TXT_FOR_SPM} \
#     --model_prefix=${OUTPUT_DIR}/pali_spm${SUFFIX} \
#     --vocab_size=4000 --character_coverage=1.0

invoke train-spm    --input=${OUTPUT_DIR}/${TXT_FOR_SPM} \
                    --model-prefix=${OUTPUT_DIR}/pali_spm${SUFFIX} \
                    --vocab-size=4000 

# echo Tokenizing the corpus for FastText
# time cat ${OUTPUT_DIR}/${TXT_FOR_SPM} | spm_encode \
#     --model=${OUTPUT_DIR}/pali_spm${SUFFIX}.model > ${TOKENIZED}

invoke encode-for-fasttext  --input-path=${OUTPUT_DIR}/${TXT_FOR_SPM} \
                            --model-path=${OUTPUT_DIR}/pali_spm${SUFFIX}.model \
                            --output-path=${TOKENIZED}

echo Training a FastText model
time ${FASTTEXT_BINARY} skipgram \
    -input ${TOKENIZED} \
    -output ${OUTPUT_DIR}/pali_fasttext${SUFFIX}