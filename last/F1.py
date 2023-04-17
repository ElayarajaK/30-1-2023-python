with open("test_1.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")



with open("test_1.txt",'w',encoding = 'utf-8') as f:
    f.write('This text has to be appended at the end')
print("Done")