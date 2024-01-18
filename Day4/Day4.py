
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
first = "Thirty"
sec = "Days"
thir = "Of"
four = "Python"
space = " "
print(first + space + sec + space + thir + space + four)

thi = "Coding"
fou = "For"
na = "All"
company = thi + space + fou + space + na
print(len(company))
print(company)
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
result = company[0:6]
print(result)
nResult = (company.find("coding"))
print(nResult)
print(company.replace("Coding", "Python"))
print(company.split(" "))
ncompany = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(ncompany.split(", "))
print(company[0])
print(len(company) -1)
print(company[10])
necompany = company.replace("Coding", "Python")
print(necompany[0:15:7])
print(company[0:15:7])
print(company.index("C"))
print(company.rfind("l"))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word = "You cannot end a sentence with because because because is a conjunction"
print(word.index("because"))
print(word.rindex("because"))
print(word[31:54])
print(word.find("because"))
print(company.startswith("Coding"))
print(company.endswith("Coding"))
newCompany = "'   Coding For All      ' "
print(newCompany.strip("  ' "))
v = "30DaysOfPython"
u = "thirty_days_of_python"
print(v.isidentifier())
print(u.isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(lib))

print("I am enjoying this challenge.\nI just wonder what is next.")
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Hassan\t25\tNigeria\tIbadan")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area}")

d = 8
f = 6
ans = d + f
anss = d - f
ansm = d * f
ansd = d / f
ansmo = d % f
ansf = d // f
anse = 8 ** 6
print(f"{d} + {f} is {ans}")
print(f"{d} - {f} is {anss}")
print(f"{d} * {f} is {ansm}")
print(f"{d} / {f} is {ansd}")
print(f"{d} % {f} is {ansmo}")
print(f"{d} // {f} is {ansf}")
print(f"{d} ** {f} is {anse}")
