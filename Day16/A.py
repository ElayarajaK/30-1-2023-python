class College:
    def __init__(self,name,address):
        self.name=name;
        self.address=address;
    def print(self):
        print("my college name : ",self.name," from : ",self.address)




obj = College("Anna univ","chennai");
obj.print();
obj1 = College("IIT","kgiri");
obj1.print();
'''
obj = College();
obj1= College();
print(obj)
print(obj1)
'''

