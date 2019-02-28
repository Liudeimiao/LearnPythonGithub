
# 类的写法，属性的写法，方法的写法
# 属性不被修改 java 中 用 final ，python 中 属性前面  __ 两个短下划线

class Player():

    def __init__(self,name,age,tel):  # 相当于 java 的构造方法
        self.__name = name  ##
        self.age = age
        self.tel = tel

    def print_role(self): # 定义一个类的方法
        print('介绍自己 %s %s %s '%(self.__name,self.age,self.tel))

    def updateName(self,newname):
        self.name = newname


user1 = Player('tom',18,'110')
user1.updateName('jack')
user1.print_role()
