name=["raja","vickram","adithya","chola"]

print(name)
#name.remove("ram");## if cheking values are there remove method will remove from the list
#if there will be no val throw Error
Element =input("Eneter the removing element from the list : ")

for a in range(len(name)):
    if(Element == name[a]):
        name.remove(Element)
    

    

print(name)
