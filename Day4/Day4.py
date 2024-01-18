
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