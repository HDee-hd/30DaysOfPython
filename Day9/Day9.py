user = 'James'
access_level = 3
isMarried = True
if user == 'admin' or access_level >= 4 or isMarried == False:
        print('Access granted!')
else:
    print('Access denied!')

Name  = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
        print("Enter your Name: ", Name)
        print("Enter your age: ", age)
        print("Dear ", Name, "You're eligible to drive!")
else:
        print("Enter your Name: ", Name)
        print("Enter your age: ", age)
        print("Dear ", Name, "You're not eligible to drive!")

my_age = int(input("Enter your age: "))
old = my_age - age
young = age - my_age
if my_age > age: 
        print("Enter your age: " , my_age)
        print(f"You are {old} years older than me.")
elif my_age < age:
        print("Enter your age: " , my_age)
        print(f"You are {young} years younger than me.")
else: print("We're the same age")