person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])

# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'Name': 'Spike',
    'color': 'Brown',
    'breed': 'Caucasian',
    'legs': 4,
    'age': 8
        }
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, 
# country, city and address as keys for the dictionary
std_dic = {
    'first_name': 'Lola',
    'last_name': 'Dumebi',
    'gender': 'Female',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Javascript', 'Python', 'MySQL'],
    'country': 'Nigeria',
    'city': 'Illy',
    'address': {
        'street': 'Behind Iya Yusuf',
        'Area': 'Tanke Tipper garage'
    }
    
}
# Get the length of the student dictionary
print(len(std_dic))
# Get the value of skills and check the data type, it should be a list
print(std_dic.get('skills'))

# Modify the skills values by adding one or two skills
std_dic['skills'].append('Django')
print(std_dic)
# Get the dictionary keys as a list
print(std_dic.keys())

# Get the dictionary values as a list
print(std_dic.values())
# Change the dictionary to a list of tuples using items() method
print(std_dic.items())
# Delete one of the items in the dictionary
print(std_dic.pop('city'))
# Delete one of the dictionaries
del dog