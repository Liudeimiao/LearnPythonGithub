import re
def parse(text, word_cnt):
    # 转为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = re.findall(r'\w+', text)  # 正则表达式 匹配
    # 更新单词和词频的字典
    for word in word_list:
        word_cnt[word] = word_cnt.get(word,0) + 1 #  字典 .get(word,0) 默认值为0 +1
    return word_cnt

# 初始化字典
word_cnt = dict()
with open('in.txt', 'r') as fin:
    for text in fin.readlines():
        word_cnt = parse(text, word_cnt) # 一行一行读取，每行统计为一个字典。
        print(len(word_cnt))

# 按照词频排序
sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

# 导出
with open('outHomework.txt', 'w') as fout:
    for word, freq in sorted_word_cnt:
        fout.write('{} :{}\n'.format(word, freq))





