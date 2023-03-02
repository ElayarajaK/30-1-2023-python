class RajA:
    A_name="Raj Aparment";
    Address="Thiruvanmiur";
    rent=7000;
    def __init__(self,house_no,hname,oters,EBUnit,Total):
        self.house_no=house_no;
        self.hname=hname
        self.oters=oters
        self.EBUnit=EBUnit*7;
        self.Total=RajA.rent+oters+(EBUnit*7)
    def printDetails(self):
        print("App name",self.A_name,"Address : ",self.Address,"No : ",self.house_no," name : ",self.hname," Total rent : ",self.Total)

houseno=input("Enter the house no ");
name =input("Enter the house name ");
maintance =int(input("Enter maintainence "))
unites =int(input("Enter Eb unites "))

obj = RajA(houseno,name,maintance,unites,0);
obj.printDetails();