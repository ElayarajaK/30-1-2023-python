data = open("data_1.txt", "r+")
file_data = data.read(10) # read 18 byte only
print("current position after reading 27 byte :",data.tell())
data1=data.seek(1) #here current position set to 0 (starting of file)
print(data1)
print("begining",data.tell())
full_data = data.read() #read all byte
print(file_data)
print(full_data)
print("position after reading file : ",data.tell())
data.close()
