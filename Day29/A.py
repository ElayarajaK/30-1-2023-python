value1 = {"raja",10,20,True,"kamal"};
value2={"raja",100,200,10,"java","python"};

print(value1.union(value2))
print("===========End 0=================");
print(value1.intersection(value2))

print("===========End 1=================");
print(value1.difference(value2));
print("===========End 2=================");
print(value2.difference(value1))
print("===========End 3=================");
print(value2.symmetric_difference(value1))
print("===========End 4 =================");
print(value1.symmetric_difference(value2))
print("===========End 5 =================");

print(value1|value2);#u
print(value1&value2);#I
print(value1^value2);#s_diff
print(value1-value2);#diff

print(type(value1));
print(value1)

print(len(value1))


print("==========================");

list1=[10,20,30,40,50]
fz=frozenset(list1);
print(fz);
print(len(fz));
print(fz|value1);
del fz;
print(fz)