#!/bin/bash    
#PBS -l select=1:ncpus=160
OMP_WAIT_POLICY=PASSIVE 
OMP_NUM_THREADS=1
cd /homes/nehrdich/paltok/src
/homes/nehrdich/miniconda3/bin/invoke \
    create-pali-all-tsv \
    --json-dir="/homes/nehrdich/paltok/segmented-pali/inputfiles" \
    --tsv-dir="/tier2/ucb/nehrdich/pli/pali_all"