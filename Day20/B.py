class College:
    c_id=30111;
    c_name="IIT";
class Staff1(College):
    s_name="APJ"
    s_salary="300000"


obj = Staff1();

print(obj.c_name+",",obj.c_id,",",obj.s_name,",",obj.s_salary)

obj1 = College();
print(obj1.c_id,",",obj1.c_name,",",obj1.s_name)