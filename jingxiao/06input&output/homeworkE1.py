import  re

def parse(text,word_dict):
    #转小写
    text = text.lower()
    #生成list
    word_list = re.findall(r'\w+',text)  #正则表达式 生成list 不要忘记 \

    #统计词频
    for word in word_list:
        word_dict[word] = word_dict.get(word,0)+1
    return word_dict

#初始化字典
word_dict = {}

with open('in.txt','r') as fin:
    for text in fin.readlines(): #按行读取
        word_dict = parse(text,word_dict)

#排序

sort_dict = sorted(word_dict.items(),key= lambda item:item[1],reverse=True) # 降序

#导出
with open('outE1.txt','w') as fout:
    for word,freq in sort_dict:
        fout.write('{} {}\n'.format(word,freq))
