count = 0
while count < 5:
    print(count)
    count = count + 1
# else:
#     print(count)

# count = 0
# while count < 5:
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1

    language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])


    numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)


for i in range(0, 11):
    print(i)
else:
    print("The last number is ", i)

c = 0
while c < 11:
    print(c)
    c = c + 1

f = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for f in f:
    print(f)

g = 10
while g >= 0:
    print(g)
    g = g -1

for i in range(1, 8):
    print('#' * i)

for i in range(9):
    for j in range(9):
        print('#', end="")
    print()

for i in range(11):
    ans = i * i
    print(f"{i} x {i} = {ans}")

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

for i in range(0, 101, 2):
    print(i)

for i in range(1, 101, 2):
    print(i)

sum = 0
for i in range(101):
    sum += i
print("The sum of all value is: ", sum)


# Initialize sum variable
total_sum = 0

# Iterate from 0 to 100
for i in range(0,101,2):
    total_sum += i

# Print the sum
print("The sum of even numbers from 0 to 100 is:", total_sum)


ans = 0
for i in range(1,101,2):
    ans += i
print("The sum of all odd number from 0 - 100 is:", ans)
