# coding=utf-8
import json

# from sanic import Sanic
#
# from module.cors import add_cors_headers
# from module.options import setup_options
# from module.wrap import wrap

# app = Sanic('test')
# app.register_listener(setup_options, "before_server_start")
# app.register_middleware(add_cors_headers, "response")

# @app.post('/test')
# @wrap()
# async def test(request):
#     print(request)
#     return request
#
#
# if __name__ == '__main__':
#     app.run(access_log=True, debug=True)

# synonyms

# from synonyms import synonyms
# # from sanic import json
# # from ujson import dumps
# from json import dumps

# [key, value] = synonyms.nearby('农业', 10)
# print(key, value)
# for index, item in enumerate(value):  # 转字符
#     value[index] = str(item)
#     # TypeError: 0.56227165 is not JSON serializable
#     # TypeError: Object of type float32 is not JSON serializable

# result = dict(zip(key, value))

# print(dumps(result, ensure_ascii=False))

# [key1, value1] = synonyms.seg("")
# print(key1, value1)
# result1 = dict(zip(key1, value1))

# print(dumps(result1, ensure_ascii=False))

# import os
# print(os.environ.copy())

# import sys
# from module.get_opts import get_opts

# argv = sys.argv
# opts = get_opts(['host', 'port'])
# # print(opts)
# HOST = opts.get('host')
# PORT = int(opts.get('port') or 8001)

# print(HOST, PORT)

from synonyms import synonyms
import jieba

from module.suggest_split import suggest_split

suggest_split()

print(jieba.lcut('工具包'))
print(synonyms.seg('工具包'))

# print('test: '+str(json_error))
