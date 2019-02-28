# fd = open("name.txt",encoding="UTF-8")
#
# try:
#     for line in fd:
#         names = line.split("|")
#         for n in names:
#             print(n)
# finally:
#     fd.close()


#自定义上下文 管理器
with open("name.txt",encoding="UTF-8") as f:

    for line in  f:
        names  = line.split("|")
        for n in  names:
            print(n)