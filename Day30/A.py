'''
def fun1():
    print("fromfun ");
    fun1()

'''
'''
print(1);
fun1();
print("End");
'''
'''
print(1)
print(10/0);
print("End")
'''
#print(1);
#print(10/0)
print(1)
list=[10,20,30]
try:
    print(list[10])
except IndexError as error:
    print(error)

print("Ending")