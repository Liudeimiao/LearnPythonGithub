#
# name = input('your name:')
# gender = input('you are a boy?(y/n)')
#
# ##### 输入 ######
# # your name:Jack
# # you are a boy?
#
# welcome_str = 'Welcome to the matrix {prefix} {name}.'
# welcome_dic = {
#     'prefix': 'Mr.' if gender == 'y' else 'Mrs',
#     'name': name
# }
#
# print('authorizing...')
# print(welcome_str.format(**welcome_dic))
#
# ########## 输出 ##########
# # authorizing...
# # Welcome to the matrix Mr. Jack.
#
#
# first = input('input one number:')
# second = input('input seconde number')
#
# # type(first) # type 函数，查看变量类型
# result = 'two number plus result is {finalResult}'
# process_result = {
#     'finalResult':int(first)+int(second) #  将 字符串转为 int 类型
# }
#
# print('authorizing...')
# print(result.format(**process_result))
#
#

# a = input('输入个数呗')
# # 1
# b = input()
# # 2
#
# print('a + b = {}'.format(a + b))
# ########## 输出 ##############
# # a + b = 12
# print('type of a is {}, type of b is {}'.format(type(a), type(b)))
# ########## 输出 ##############
# # type of a is <class 'str'>, type of b is <class 'str'>
# print('a + b = {}'.format(int(a) + int(b)))
# ########## 输出 ##############
# # a + b = 3

import re


# 你不用太关心这个函数
# def parse(text):
#     # 使用正则表达式去除标点符号和换行符
#     text = re.sub(r'[^\w ]', '', text)
#
#     # 转为小写
#     text = text.lower()
#
#     # 生成所有单词的列表
#     word_list = text.split(' ')
#
#     # 去除空白单词
#     word_list = filter(None, word_list)
#
#     # 生成单词和词频的字典
#     word_cnt = dict()
#     for word in word_list:
#         if word not in word_cnt:
#             word_cnt[word] = 0
#         word_cnt[word] += 1
#
#     # 按照词频排序
#     sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
#
#     return sorted_word_cnt
#
#
# with open('in.txt', 'r') as fin:
#     text = fin.read()
#
# word_and_freq = parse(text)
#
# with open('out.txt', 'w') as fout:
#     for word, freq in word_and_freq:
#         fout.write('{} {}\n'.format(word, freq))
#
# ########## 输出 (省略较长的中间结果) ##########



# def parseTest(text):
#     #使用正则表达式去除标点符号和换行符
#     text = re.sub(r'[^\w ]', '', text)
#
#     #转为小写
#     text = text.lower()
#
#     #生成所有单词的列表
#     word_list = text.split(' ')
#
#     #去除空白单词
#     word_list = filter(None,word_list)
#
#     #生成单词和词频字典
#     word_cnt = dict()
#     for word in word_list:
#         if word  not in word_cnt:
#             word_cnt[word] = 0
#         word_cnt[word] += 1
#
#
#     # 按照词频排序

#     #sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
#     sorted_word_cnt = sorted(word_cnt.items(),key=lambda  kv:kv[1],reverse=True)
#
#     return sorted_word_cnt
#
# with open('in.txt','r') as fileIn:
#     text = fileIn.read()
#
# word_and_freqText = parseTest(text)
#
# with open('out2.txt','w') as fileOut:
#     for word,freqT in word_and_freqText:
#         fileOut.write('{},{}\n'.format(word,freqT))

# import json
#
# params = {
#     'symbol': '123456',
#     'type': 'limit',
#     'price': 123.4,
#     'amount': 23
# }
#
# params_str = json.dumps(params)
#
# print('after json serialization')
# print('type of params_str = {}, params_str = {}'.format(type(params_str), params))
#
# original_params = json.loads(params_str)
#
# print('after json deserialization')
# print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

########## 输出 ##########


# paramsTest = {
#     'symbol':'123456',
#     'type':'limit',
#     'price':123,
#     'amount':23
# }
#
# paramsTest_str = json.dumps(paramsTest)
#
# print('after json serialization')
# print('type of paramsTest = {} ,paramsTest_str = {}'.format(type(paramsTest_str),paramsTest_str))
#
# original_paramsTest = json.loads(paramsTest_str)
#
# print('after json deserialization')
# print('type of original_paramsTest= {},original_paramsTest={}'.format(type(original_paramsTest),original_paramsTest))



import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

# with open('params.json', 'w') as fout:
#     params_str = json.dump(params, fout)
#
# with open('params.json', 'r') as fin:
#     original_params = json.load(fin)
#
# print('after json deserialization')
# print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

########## 输出 ##########

# after json deserialization
# type of original_params = <class 'dict'>, original_params = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}


with open('paramsTest.json','w') as fTestOut:
    paramsTest_str = json.dump(params,fTestOut) #  TypeError: dumps() takes 1 positional argument but 2 were given

with open('paramsTest.json','r') as fTestIn:
    originalTest_params  = json.load(fTestIn)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(originalTest_params), originalTest_params))