                

# Write a python comment saying 'Day 2: 30 Days of python programming'
# Declare a first name variable and assign a value to it
# Declare a last name variable and assign a value to it
# Declare a full name variable and assign a value to it
# Declare a country variable and assign a value to it
# Declare a city variable and assign a value to it
# Declare an age variable and assign a value to it
# Declare a year variable and assign a value to it
# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
# Declare multiple variable on one line


#Day 2: 30 Days of python programming'
first_name = "Hassan"
last_name = "Dairo"
full_name = "Hassan Dairo"
country = "Nigeria"
city = "Ilorin"
age = 28
year = 2024
is_married = True
is_true = True
is_light_on = True
newName, newLastname, newage = "Mustopha", "Ahmad", 90


# Check the data type of all your variables using type() buHassanilt-in function
print(type(first_name));
print(type(last_name));
print(type(full_name));
print(type(country));
print(type(city));
print(type(age));
print(type(year));
print(type(is_married));
print(type(is_true));
print(type(is_light_on));
print(type(newName));
print(type(newLastname));
print(type(newage));

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
fname = len(first_name)
lname = len(last_name)

if(fname > lname):
    print("Your first name is longer")

else:
    print("Your last name is longer")

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
num_ans = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
num_sub = num_two - num_one

# Multiply num_two and num_one and assign the value to a variable product
mum_mult = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
mum_div = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
mum_mod = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
mum_pow = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
mum_floor = num_one // num_two

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.

radius = 30
pi = 3.142
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print("The area of this circle is: ", area_of_circle)

radi = int(input("Enter radius: "))
area_of_circle = pi * radi ** 2

print("The circumference of this circle is: ", circum_of_circle)
print("The area of the second circle is: ", area_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter first name: ")
last_name = input("Last name: ")
country = input("your country: ")
age = input("Your age: ")

print(first_name)
print(last_name)
print(country)
print(age)

help()

