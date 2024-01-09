# Day 1 30DaysOfJavaScript
import sys
print(sys.version)

# Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
# subtraction(-)
# multiplication(*)
# modulus(%)
# division(/)
# exponential(**)
# floor division operator(//)
print(2 + 3)    
print(3 - 1)
print(2 * 3)
print(3 / 2)
print(3 ** 2)
print(3 % 2)
print(3 // 2)


# Write strings on the python interactive shell. The strings are the following:
# Your name
# Your family name
# Your country
# I am enjoying 30 days of python

print("Hassan")
print("Dairo")
print("Nigeria")
print("I am enjoying 30 Days of python")


# Check the data types of the following data:
# 10
# 9.8
# 3.14
# 4 - 4j
# ['Asabeneh', 'Python', 'Finland']
# Your name
# Your family name
# Your country

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Hassan', 'Python', 'Nigeria']))
print(type("Hassan"))
print(type("Dairo"))
print(type("Nigeria"))


# Find an Euclidian distance between (2, 3) and (10, 8)

import math

def eu_distance(point1, point2):
    p1, q1 = point1
    p2, q2 = point2
    distance = math.sqrt((p2 - p1)**2 + (q2 - q1)**2)
    return distance

point_a = (2, 3)
point_b = (10, 8)

distance = eu_distance(point_a, point_b)
print(distance)
 