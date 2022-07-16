# coding=utf-8
from sanic import Sanic
from synonyms import synonyms
# from jieba import synonyms.jieba
# from orjson import loads  # 需要一个>3.8.5+ 且<3.9的64位Python
# from module.cors import add_cors_headers
# from module.options import setup_options
from module.suggest_split import suggest_split
from module.wrap import wrap
from sanic.log import logger
from module.get_opts import get_opts

app = Sanic("synonyms_web")

# app.register_listener(setup_options, "before_server_start")
# app.register_middleware(add_cors_headers, "response")


@app.post('/synonyms_nearby')
@wrap()
async def synonyms_nearby(request):
    keyword = request['keyword']
    size = request.get('size', 10)
    [key, value] = synonyms.nearby(keyword, size)
    for index, item in enumerate(value):  # 转字符
        value[index] = str(item)

    result = dict(zip(key, value))
    return result


@app.post('/synonyms_seg')
@wrap()
async def synonyms_seg(request):
    keyword = request['keyword']
    [key, value] = synonyms.seg(keyword)
    # print([key, value])
    result = dict(zip(key, value))
    # print(result)
    return result


@app.post('/test')
@wrap()
async def test(request, response):
    print("response: ", response)
    return request.json()


opts = get_opts(['host', 'port'])
HOST = opts.get('host')
PORT = int(opts.get('port') or 8001)

suggest_split()

if __name__ == '__main__':
    app.run(debug=False, access_log=False, host=HOST, port=PORT)
    # print('start: host=%s,port=%s' % (HOST, PORT))
