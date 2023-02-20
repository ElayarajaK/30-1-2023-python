Marks1= int(input("Eneter marks1"))

Marks2= int(input("Eneter marks1"))



def findMax(mark1,mark2):
    max=mark1 if mark1>mark2  else mark2;
    return max;

MaxValue = findMax(Marks1,Marks2);
print(MaxValue);