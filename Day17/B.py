'''
1.what is mean class and waht is mean  object
2.when constructer is execute
3.y the constructer is importent



'''
static variable
instance variable

class Student:
    def __init__(self,name,id,address,marks):
        self.name=name;
        self.id=id;
        self.address=address;
        self.marks=marks;
    
    def printVal(self):
        print(self.name,self.id,self.address,self.marks)
std1 = Student("Raja",20111,"chennai",200);
std2 = Student("java",20111,"chennai",200);
std3 = Student("vickram",20111,"chennai",200);
std4 = Student("study",20111,"chennai",200);
std5 = Student("jhon",20111,"chennai",200);
std1.printVal();
std2.printVal();
std3.printVal();
std4.printVal();
std5.printVal();

'''
print(std1.name)
print(std1.id)
print(std1.address)
print(std1.marks)

print(std2.name,std3.name,std4.name,std5.name)
'''