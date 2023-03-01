class Teacher:
    college_name="IIT";
    college_id=201001;
    def __init__(self,t_name,t_dep,salary,cname,cid):
        self.t_name=t_name;
        self.t_dep=t_dep;
        self.salary=salary;
        college_name=cname;
        college_id=cid;
    def printVal(self):
        print(self.t_name,self.t_dep,self.salary,self.college_name,self.college_id)

staff1=Teacher("raj","CSC",20000,"AU",302220);
staff1.printVal();

print(Teacher.college_name)
#print(Teacher.salary)
print(staff1.college_name)
print(college_name)