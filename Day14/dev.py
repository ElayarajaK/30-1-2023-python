value1 = int(input("Enter the 1st val :"));
value2 = int(input("Enter the 1st val :"));
print("Before swaping -> value1 : ",value1,", value 2 : ",value2)
def Swaping(arg1,arg2):
    '''temp = arg1;
    arg1 = arg2;
    arg2 =temp;'''
    arg1 = arg1+arg2;
    arg2 = arg1-arg2;
    arg1 = arg1-arg2;
    return "Value1 : ",arg1,"value 2 : ",arg2;
swaped = Swaping(value1,value2);
print(swaped);