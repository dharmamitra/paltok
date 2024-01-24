WORK_DIR=$(pwd)
OUTPUT_DIR=$(realpath ${WORK_DIR}/..) #"/output/"
TASKS=$(realpath ${OUTPUT_DIR}/src)
SRC_DIR=${OUTPUT_DIR}/src

FASTTEXT_BINARY=${WORK_DIR}/../../fastText/fasttext


mkdir -p ${OUTPUT_DIR}

cd ${SRC_DIR}

# invoke create-pali-all-tsv \
#     --json-dir ${OUTPUT_DIR}"/segmented-pali/inputfiles/" \
#     --tsv-dir ${OUTPUT_DIR}

invoke prep-spm --src-dir=${OUTPUT_DIR}

INPUT=$1
if [ -z $INPUT ]; then
    INPUT=$(invoke print-txt-for-spm ${OUTPUT_DIR})
fi
echo INPUT = $INPUT
SUFFIX=$(invoke print-timestapm --path $INPUT)
echo $SUFFIX
TXT_FOR_SPM=${OUTPUT_DIR}/$INPUT
TOKENIZED=${OUTPUT_DIR}/pali_tokenized_for_fasttext${SUFFIX}.txt

time spm_train --input=${TXT_FOR_SPM} \
    --model_prefix=${OUTPUT_DIR}/pali_spm${SUFFIX} \
    --vocab_size=4000 --character_coverage=1.0

echo Tokenizing the corpus for FastText
time cat ${TXT_FOR_SPM} | spm_encode \
    --model=${OUTPUT_DIR}/pali_spm${SUFFIX}.model > ${TOKENIZED}

echo Training a FastText model
time ${FASTTEXT_BINARY} skipgram \
    -input ${TOKENIZED} \
    -output ${OUTPUT_DIR}/pali_fasttext${SUFFIX}.model