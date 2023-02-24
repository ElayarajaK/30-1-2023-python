Student_list=[10,20,30,45,65,75]

def even(value):
    if(value%2==0):
        return True
    else:
        False

retvalue =list(filter(even,Student_list));
print(retvalue)

valuesof =list(filter(lambda name:name > 40 , Student_list))
print(valuesof)

