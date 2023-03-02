'''
instance method
static method
class method
'''

class B:
    def __init__(self) -> None:
        pass

    def method2(self):
        print("print instance meth");
    @classmethod
    def method(a):
        print("class method")
    @staticmethod
    def smethod():
        print("print static method")
    



obj = B();

obj.method();
obj.smethod();
B.smethod();
B.method();
obj.method2();
B.method2();