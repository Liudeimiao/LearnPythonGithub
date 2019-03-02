from urllib import request

url ='http://www.baidu.com'
response = request.urlopen(url,timeout=1) # 打开url ，超时 1秒 就停掉。
print (response.read().decode('utf-8')) # 解码要用utf-8

