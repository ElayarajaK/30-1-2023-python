''' var-arg funtion '''
'''

def addition(*name1):
   
    for temp in range(len(name1)):
        print(name1[temp])



def addition(*name1):
    print(len(name1))
'''
def addition(*name1):
    print(name1)

addition("Raja")
addition("Raja","kamal")
addition(100,"Java","Indian")
addition(100,True,"Python","USA")


name1=10;
name2=20;

swap(name1,name2)