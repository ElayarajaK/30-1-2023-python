f_name="raja";
class car:
    def __init__(self,name,price) :
        self.c_name=name;
        self.price=price;
    def printData(self):
        print(self.c_name,",",self.price)

class Employee:
         name=None;
         ESalary=None;
         typeCar=None;
         def __init__(self,name,Esalary,typecar):
              self.name=name;
              self.ESalary=Esalary;
              self.typeCar =typecar;
         def printData(self):
            print(self.name,"n",self.ESalary,",",self.typeCar.c_name,",",self.typeCar.price)
             
variable_name =car("Tata",3000);
obj1=Employee("jhon",30000,variable_name);
obj1.printData();
variable_name.printData();


#single inheritance
class B:
     id=2011101;
class C(B):
     names="Jhon";

#multilevel
class x1:
     name="x1";
class x2(x1):
     id=201130001;
class x3(x2):
     salary=30000;
class x4(x3):
     address="chennai"

##multiple inheritance
class m1:
     std_id=201100;
class m2:
     std_name="Raj";
class m3(m1,m2):
     std_marks=300;
#hyharical inheritance
class h1:
     h_name="python"
class h2(h1):
     h_salary=40000;
class h3(h1):
     h_address="banglore";
     
