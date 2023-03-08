class A(object):
    def __init__(self):
        print("Hello i am from A")
    def __init__(self,name):
        self.name=name;
        print("Hello i am from A",name)
        super().__init__();
   
class B(A):
    def __init__(self):
        super().__init__("rajas")
        


obj = B();