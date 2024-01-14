# Declare your age as integer variable
age = 29

# Declare your height as a float variable
my_height = 173.2

# Declare a variable that store a complex number
vec = 1 + 2j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
tri_height = int(input("Enter height: "))
area_of_tri =  0.5 * base * tri_height
print('Area of the triangle is: ', area_of_tri)


# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a =  int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

peri_of_tri = side_a + side_b + side_c
print('The perimeter of the triangle is: ',peri_of_tri , 'cm')

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_rec = int(input("Enter the lenght: "))
width_rec = int(input('Enter the width: '))

peri_of_rec = 2 * (length_rec + width_rec)
area_of_rec = length_rec * width_rec
print('The perimeter of the rectangle is: ', peri_of_rec)
print('The area of the rectangle is: ', area_of_rec)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = int(input('Enter radius: '))
pi = 3.142
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print("The area of this circle is: ", area_of_circle)
print("The circumference of the circle is: ", circum_of_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_m = 2
y_intercept = -2
x_intercept = y_intercept/slope_m

print(f"Slope: {slope_m}, x_intercept: {x_intercept}, y_intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
def eu_distance(point1, point2):
    p1, q1 = point1
    p2, q2 = point2
    distance = math.sqrt((p2 - p1)**2 + (q2 - q1)**2)
    return distance
point_a = (2, 2)
point_b = (6, 10)

distance = eu_distance(point_a, point_b)
print('The Euclidean distance is: ', distance)

def slope_(point1, point2):
    p1, q1 = point1
    p2, q2 = point2
    slope = (q2 - q1)/(p2 - p1)
    return slope

slope = slope_(point_a, point_b)  
print('The slope is: ',slope)

# Compare the slopes in tasks 8 and 9.
print(slope_m > slope)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

def formula(x):
    return x**2 + 6*x + 9

x_value_for_zero_y = [x for x in range(-10, 11) if formula(x) == 0]

print('Y would be Zero when X is: ', x_value_for_zero_y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len("python") > len("dragon"))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

print("on is in both python and dragon " , "on" in "python" and "dragon" )

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print("Jargon is in the statement? ", "jargon" in "I hope this course is not full of jargon")

# Find the length of the text python and convert the value to float and convert it to string

tex = len('python')
print(str(float(tex)))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def even_no(number):
    return number % 2 == 0

number = int(input("Enter a number: "))
if (number == 0):
    print("{number} is an even number")
else:
    print(f"{number} is an odd number!")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
val = int(2.7)
floor_div = 7 // 3

print(floor_div == val)

# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Check if int('9.8') is equal to 10
vale = float('9.8')
print(int(vale) == 10)

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Hour = int(input("Enter Hours: "))
rate = int(input("Enter rate in $$: "))

weekly_earning = Hour * rate
print("Enter hours: ", Hour)
print("Enter rate per hour: ", rate)
print("Your weekly earning is: ", weekly_earning)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter the number of years you have used: "))
lived = years * 365 * 24 * 60 * 60

print('Enter the number of years you have lived: ', years)
print(f'You have lived for {lived} seconds')

# Define the number of rows for the table
num_rows = 5

# Print the table
for i in range(1, num_rows + 1):
    print(f"{i} 1 {i} {i*i} {i*i*i}")
