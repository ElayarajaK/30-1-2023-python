'''
if condition
  if the condition is true if block will execute the condition is false it will execute
'''

age = int(input("Enter your age"));

if age>=18 and age <=100:
    print("Your eligible for vote")
elif age > 100:
    print("expired")
else:
    print("your not eligible for vote")
