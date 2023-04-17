class AgeInvalidError(Exception):
    def __init__(self, msg):        
        super().__init__(msg)

age =int(input("Enter the age"))
if(age < 20):
        try:
            raise AgeInvalidError("Age should be above 20");
        except AgeInvalidError as msg:
             print(msg)


else:
     print("Voting progress...");


print("Done")