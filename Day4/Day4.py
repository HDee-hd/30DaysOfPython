
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
