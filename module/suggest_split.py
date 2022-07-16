import re
import yaml
import jieba


def suggest_split():
    arr = yaml.safe_load(open('./data/拆分词.yaml'))
    for s in arr:
        split_list = re.split(r'[\s|,|\-/]', s)
        # print('jieba suggest: ', split_list)
        jieba.suggest_freq(tuple(split_list), True)
    print('jieba suggest split started')
