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
        
        print(f"You are {old} years older than me.")
elif my_age < age:
        
        print(f"You are {young} years younger than me.")
else: print("We're the same age")

#Number 3
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
        print(f"{a} is greater than {b}")
elif a < b:
        print(f"{a} is smaller than {b}")
else: print(f"{a} is equal to {b}")
# Number 4
score = int(input("Enter your Score: "))
if score >= 80:
        print("You're on grade A")
elif score >= 70:
        print("You're on grade B")
elif score >= 60:
        print("You're on grade C")
elif score >= 50:
        print("You're on grade D")
elif score >= 0:
        print("You're on grade B")