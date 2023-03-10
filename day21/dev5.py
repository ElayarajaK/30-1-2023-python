class Employee:
    __eid=20111;
    __ename=None;
    __eaddress=None;
    __salary=None;

    def __init__(self):
        pass
    def __init__(self,eid,ename,eaddress,salary):
        self.__eid =eid 
        self.__ename=ename 
        self.__eaddress=eaddress 
        self.__salary=salary
    def setId(self,id):
        self.__eid=id;
    def getId(self):
        return self.__eid;
    def setname(self,name):
        self.__ename=name;
    def getName(self):
        return self.__ename;
    def setAdd(self,add):
        self.__eaddress=add;
    def getAdd(self):
        return self.__eaddress;
    def setSalary(self,salary):
        self.__salary=salary;
    def getSalary(self):
        return self.__salary;


        