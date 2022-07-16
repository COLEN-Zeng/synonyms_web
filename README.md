# synonyms-web

1. [描述]:
   主要基于 synonyms 库的 python web 程序
   中文近义词库地址：https://github.com/chatopera/Synonyms
2. [环境]:
   python 3.7+、node 10+、pm2、yarn、pip3
   1. 进入虚拟环境 sh ./virtualenv_activate.sh
   2. 安装依赖 python3 -m pip install --upgrade pip && pip install -r requirements.txt
   3. data/words.vector.gz 下载词库: https://gitee.com/chatopera/cskefu/attach_files/610602/download/words.vector.gz
   4. Apple Silicon 需通过 miniforge 安装 python3.9：https://github.com/conda-forge/miniforgegitee
3. [项目结构简介]:

```
   .
   ├── README.md
   ├── data
   │ ├── stopwords.txt
   │ ├── vocab.txt
   │ ├── words.vector.gz 词库地址(自行下载)：https://gitee.com/chatopera/cskefu/attach_files/610602/download/words.vector.gz
   │ └── 拆分词.yaml # 强制拆分词配置文件 需要拆分的关键字可添加到此处
   ├── main.py # 程序入口
   ├── module
   ├── package.json # node 依赖
   ├── requirements.txt # python 依赖
   ├── run.sh # 运行脚本
   ├── toolchain
   │ └── deploy # 发布配置 easy-deploy-tool: https://github.com/qw623577789/easy-deploy
   ├── virtualenv_activate.sh # 环境激活脚本
   └── 词性表.md
```

4. [运行方式]
   ./run.sh
