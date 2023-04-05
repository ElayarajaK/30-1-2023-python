

try:
    wte=open("B.txt","r");
    wte.writelines("Hello Line")
    print(1)
    
except Exception as e:
    print(2)
    pass
else:
    print(3)
finally:
    print("Always print")
    wte.close();