#!/usr/bin/python
# 类的继承
if __name__ == '__main__':
    class Animal:
        public_val = '类的公有属性' # 类的公有属性
        __private_val = '类的私有属性' # 类的私有属性
        def __init__(self) -> None:
            self.name = '小黄'#成员公有属性
            self.__age = 3 # 成员私有属性
        def call(self):
            self.sex = 'female'

    # 子类未覆盖父类的属性和方法
    class Cat(Animal):
        def __init__(self) -> None:
            # Animal.call(self)
            Animal.call(Animal)
            # Animal.__init__(self)
            Animal.__init__(Animal)
            print(self.name)
            print(Cat.name)
            print(Animal.name)
            print(super().name)

            # 调用Animal.call(self)时，只能使用self.sex
            print(self.sex)
            print(Cat.sex) # 成员属性无法被类直接调用
            print(Animal.sex)
            print(super().sex)

            print(self.public_val)
            print(Animal.public_val)
            print(super().public_val)
            print(Cat.public_val)
            
            print(self._Animal__private_val) #类的私有属性在解析时带上了类名
            print(Animal.__dict__) #查看类各种属性的内置属性
            

    cat = Cat()
