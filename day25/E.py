name="java python angular react mysql oracle";

print(len(name))

'''
name=name.lstrip();


print(len(name))
'''

print(name.find('angular'))

checkVal=input("Enter the checking value")

if(name.find(checkVal) > 0):
    print("available")
else:
    print("Not available")
