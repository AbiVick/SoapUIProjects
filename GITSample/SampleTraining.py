
# variable in python 

# name = 'Kritika'

# print(type(name))
# print(name)

# Array/list in python 

#               0         1        2              3        4
superHero = ['SuperMan', 'Hulk', 'Capt AMerica', 'Thor', 'Sp.Man', 23423, 234234.32423, True]

# # //index 

# print(type(superHero))
# print(len(superHero))
# print(superHero[    len(superHero)  -  2     ])

print(superHero[-1])

# List example

# Append

# add item to list at the end

superHero.append('Dinesh')

print(superHero)

# //Add item to specific index 

superHero.insert(1,'Dinesh Kartik')

print(superHero)

# //validate value is present 

validateValueInList = 'Thor' in superHero

print(validateValueInList)

# Remove an item into list 

superHero.remove('Thor')

print(superHero)

# remove an item from last element 

print("====================remove an item from last element============")

removedValueFromLast = superHero.pop()

removedValue = superHero.pop(1)

print(removedValue)

print(superHero)

#delete

print("====================delete============")

print(superHero)

del superHero[0]

print(superHero)

# print("====================delete============")

# print(superHero)

# del superHero

# # print(superHero)

# print("====================clear============")

# print(superHero)

# superHero.clear()

# print(superHero)

# ====================================================

# //ctrl+/

# loops 

print("====================loop============")

superHero_update = ['SuperMan', 'Hulk', 'Capt AMerica', 'Thor', 'Sp.Man']

for x in superHero_update:

    print("Value into list: " + x )

    if('Thor' == x):

        print('finally......found the value')

    else:

        print('validation is in progress...')

# ============================================================

# hello Dinesh, welcome you in  today session

superHero_updated = ['SuperMan', 'Hulk', 'Capt AMerica', 'Thor', 'Sp.Man']

def greeting(name="Abhishek"):

    print("hello " + name + ", welcome you in  today session, my fav superHero are:  " + superHero_updated[-1])

    print(f'hello {name} welcome you in  today session, my fav superHero are: {superHero_updated[-1]}')

greeting('Charishma')        # default

greeting()                   # default

#===============================================================
