import requests
import re
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

#print(content)


# < div class ="grid-item work-thumbnail" >
# < a href="(.*?)".*?title">(.*?)</div>
# < div class ="author" > LynnWei < / div >

#正则表达式 复杂
pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)

#print(results)


for result in results:
    url, name = result
    print('链接： %s 名字: %s ' %(url, re.sub('\s', '', name))) #去掉空白行 换行符号等