print(1)
try:
    i =int(input("Hello"));
except ValueError as err:
    print(err)

print("End");

print("Begin");
try:
    name = open("A.txt","r");
    val=name.readline();
    print(val);
   
except FileNotFoundError as f:
    print(f);
print("End")

