class Student:
    def __init__(self):
        pass;
    '''
    def setName(self,name,address):
        self.name=name;
        self.address=address;
    
    def getName(self):
        return self.name +"," +self.address;
        '''
    
    def setName(self,name):
        self.name=name;
    def getName(self):
        return self.name;
    def setAddress(self,address):
        self.address = address
    def getAddress(self):
        return self.address;
   
 
''' 
   def setAddress(self,address):
        self.address = address
    def getAddress(self):
        return self.address;'''
        
obj2=Student();
#obj2.setName("Vijay","Chennai");
#print(obj2.getName())
obj2.setName("Jhon");
print(obj2.getName());
obj2.setAddress("Madurai");
print(obj2.getAddress());