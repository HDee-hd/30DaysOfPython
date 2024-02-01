# Declare an empty list
from shlex import join


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
# Add an IT company to it_companies
it_companies.append("Yahoo")

# Insert an IT company in the middle of the companies list
it_companies.insert(2, "Dell")
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)
# Join the it_companies with a string '#;  '
nnew = ["Gamers INC"]
new_it_companies = it_companies + nnew
# Check if a certain company exists in the it_companies list.
does_exist = "Dell" in new_it_companies
print(does_exist)
# Sort the list using sort() method
new_it_companies.sort()
print(new_it_companies)
# Reverse the list in descending order using reverse() method
new_it_companies.sort(reverse=True)
# Slice out the first 3 companies from the list
print(new_it_companies[:3])
# Slice out the last 3 companies from the list
print(new_it_companies[3:])
# Slice out the middle IT company or companies from the list
new_it_companies.remove("HASDEEN")
print(new_it_companies)
# Remove the first IT company from the list
print(new_it_companies[1:])
# Remove the middle IT company or companies from the list
# new_it_companies.remove("HASDEEN")
# print(new_it_companies)
# Remove the last IT company from the list
new_it_companies.remove("Amazon")
print(new_it_companies)
# Remove all IT companies from the list
new_it_companies.clear()
print(new_it_companies)
# Destroy the IT companies list
del new_it_companies
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
full_stack = front_end + back_end
print(full_stack)
# Then insert Python and SQL after Redux.
full_stack.append("Python")
full_stack.append("SQL")
print(full_stack)