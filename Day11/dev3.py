'''
    user defined funtion with arg
'''
def add(id1,id):
    print("print Val",(id+id1));

def add1():
    print("print no-arg Val");

add(10,20);
add1();
add(100,200);
add(30,30);
add(50,50);


name="raja";
s_id=30101;
subject="Math"
marks=88;
avg=55.52;
def printDetails(name,sid,sub,mar,avg):
    print("my name is : ",name,"\n and the id is : ",sid,"\n My subject was : ",sub,"\n Marks is : ",mar,"\n avg : ",avg)

printDetails(name,s_id,subject,marks,avg);