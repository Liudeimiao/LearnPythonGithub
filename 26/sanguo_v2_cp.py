import  re

#需求，统计出三国中出现人物前10 名。

def find_item( hero ):
    #打开三国
    with open('sanguo.txt',encoding="GB18030") as f:
        data = f.read().replace("\n","")
        name_num = re.findall(hero,data)
        print("主角 %s 出现次数 %s " %(hero,len(name_num)))

    return len(name_num)


find_item('葛亮')
# 读取人物的信息
#人物字典
name_dict = {}

with open('name.txt',encoding='UTF-8') as f:
    for line in  f:
        names = line.split("|")
        for name in names:
            name_num = find_item(name)
            name_dict[name] = name_num

# 不懂 todo 下面的代码
name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])



