list=[10,20,30]
print(list)
list[1]=100;
print(list)

values=10,20,30,40,50,"raja";

print(type(values));
print(values)
print(values[1])
#values[1]=200;

print(len(values))
print(values[2:5:2])


values2=30,10,5,60,70,2,60,2,60,2,70,10;
print(sorted(values2,reverse=True));
print(values2.count(70))
print("min val : ",min(values2))

print("max val : ",max(values2))

print(sum(values2));

print(values2.index(70))



t1=10,20,3,0,40;
t2=10,20,30,40;
print(t1 == t2)


