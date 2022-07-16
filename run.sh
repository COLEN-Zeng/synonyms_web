#!/bin/bash

if [ $# -eq 0 ]; then
    echo -e "USAGE:./$(basename "$0") <dev|prod>"
    exit -1
fi
ENV=$1

. ./virtualenv_activate.sh

# pip
#export SYNONYMS_WORD2VEC_BIN_URL_ZH_CN=https://gitee.com/chatopera/cskefu/attach_files/610602/download/words.vector.gz
export SYNONYMS_WORD2VEC_BIN_MODEL_ZH_CN=${PWD}/data/words.vector.gz
export SYNONYMS_WORDSEG_DICT=${PWD}/data/vocab.txt
python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# python -c "import synonyms" # download word vectors file 首次安装下载词库
# npm
yarn

# start
./node_modules/.bin/easy-deploy start toolchain/deploy/${ENV}/index.js
