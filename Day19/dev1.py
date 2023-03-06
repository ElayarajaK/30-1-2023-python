class Student:
    def __init__(self) -> None:
        pass
    
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def setValueName(self,name):
        self.name=name;
    def getValueName(self):
        return self.name;
    def setValueid(self,id):
        self.id=id;
    def getValueid(self):
        return self.id;

std1=Student("raja",11011)

print(std1.getValueName());

##print(std1.id)##in encapsulation you should not got direct acces of any field
        