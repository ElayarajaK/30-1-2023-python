marks =int(input("Enter marks"));

if(marks > 100):
    raise FileNotFoundError("Your marks should be bellow 100")