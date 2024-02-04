user = 'James'
access_level = 3
isMarried = True
if user == 'admin' or access_level >= 4 or isMarried == False:
        print('Access granted!')
else:
    print('Access denied!')