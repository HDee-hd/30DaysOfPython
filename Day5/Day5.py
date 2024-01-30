# Declare an empty list
lst = []

# Declare a list with more than 5 items
names = ["Hassan", "Olukay", "Dairo"]


# Find the length of your list
print(len(names))

# Get the first item, the middle item and the last item of the list
namess = names[0]
print(namess)



# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
nameM = ["Hassan", 12, 6.0, "Married", "52, Bakery road."]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print("Number of companies: ",len(it_companies))
# Print the first, middle and last company
print(it_companies[0:3:6])
# Print the list after modifying one of the companies
it_companies[1] = "Hasdeen"
print(it_companies)