# syntax
# Create an empty tuple
emt = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bro = ('Hassan', 'Hussayn', 'Abdullah')
sis = ("Aminat", "Aisha", "Aliya")
sibl = bro + sis
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
print("I have ", len(sibl), " siblings.")
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
fam = list(sibl)
fam.append("Dad")
fam.append("Mom")
print(fam)