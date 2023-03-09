'''
access specifier
1.private (_ _) class level field and method
2.public () you access from all the project
3.protected(_) only accesble into the child class
'''

class A:
    __name=None;
    __id=None;
    def __init__(self,name,id):
        self.__name=name;
        self.__id=id;

    def printData(self):
        print(self.__name,",",self.__id);
obj=A("Raja",20112);

print(obj.__name)
obj.printData();