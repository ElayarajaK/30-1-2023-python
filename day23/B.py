from abc import *;#abstract class

class A(ABC):
    @abstractmethod
    def method1(self):
        print("Hello");

    @abstractmethod
    def method2(self,name):
        pass

class B(A):
    def method1(self):
        return super().method1()
    def method2(self, name):
        return 0;


obj =  B();

#obj.method1();

obj.method1();