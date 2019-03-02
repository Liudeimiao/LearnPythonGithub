from urllib import parse
from urllib import request

# 封装数据 post 请求。
data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')
#
# print(data)

# 读取get 请求
# response2 = request.urlopen('http://httpbin.org/get', timeout=3) #
# print(response2.read())

#读取post 请求
response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

import urllib
import socket


try:
    response3 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')