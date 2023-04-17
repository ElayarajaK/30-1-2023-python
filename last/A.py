values=None;
try:
    file=open("abc.txt","r");
    values = file.read();

except BaseException as fn:
    print(fn);


print(values)


print("Done")
