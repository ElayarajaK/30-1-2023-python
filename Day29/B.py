value={1:"raja",2:"raja",3:"python",4:"React",5:"git","Angular":6};

#{key:value} Dict
print(value)
print(type(value));

print(value[5])
print(value)

print(value.get('Angular'));
print(len(value.keys()));
#print(value[0]);

for temp in value:
    print("Key : ",temp," and value is : ",value.get(temp));



print("===============================");

value.pop(4);

print(value)

value.clear();
print(value)