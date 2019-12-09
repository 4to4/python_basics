print("Python for Perl Developers - #")
print("------------------------------------")
print("> Tutorial for {}, {} and {}".format('List', 'Tuples', 'Sets'))

print(""""Lists:
  List are Perl arrays.
  Enclosed in square brackets '[]'.
  Separated by commas.
  Accepts mixed data types like stings, int etc.\n
  All the items are indexed and last item """)
print("""Example:
list = [ 'Python', 'Perl', 'C#', 1, 2, '1' ]\n""")

list = ['Python', 'Perl', 'C#', 1, 2, '1']
print("The list looks like => ", list)

print(""" Popular methods to use on lists are:
1. pop     - returns the last entered element in the list""")
print("Popping the last element => ", list.pop())

print("""2. append - appends a list to another list at the end""")
list.append([11, 'X'])
print("Appending '11', 22 to list, it looks like ", list)
print("------------------------------------")

print(
    """3. Copy - copies list reference if assigned to a another list variable. e.g. list = list1 will only copy the reference. Any changes to list will also be made to list1.
To make a full copy use the copy() function. e.g. list.copy(list1)""")

list1 = []
list1 = list.copy()
print("Copied list list1 looks like ", list1)
list1.append(['XXX'])
print("list1 was appended now looks like ", list1)
print("list remained unchanged ", list)
print("Iterating through the list\n")

print("""For loop by index\n""")
for i in range(0, len(list)):
    print(list[i])

# for loops by value
for i in list1:
    print("list is {}".format(i))

# for loop by index and value perl each = enumerate
for index, value in enumerate(list):
    print("Index => {} vs Value => {}".format(index, list[index]))

print(""" Tuples are C Const Arrays 
Represented by ()
cannot be modified
can be accessed like arrays """)
tup = ('a', 1, 'g')
print("Tuple is ", tup)

for i in range(0, len(tup)):
    print("Tup index => {} and value => {}".format(i, tup[i]))

print(""" Sets are Perl arrays
unordered
every element is unique
set is RW but the elemets are RO
represented by {} """)

sets = {'a', 'd'}

for i in sets:
    print("value => {}".format(i))

#cannot store dupes
sets.add('a')
sets.add('g')

for i in sets:
    print("New set value {} ".format(i))

# if a value is present set
print('a' in sets)
print('RT' in sets)

#add more than one item __import__
sets.update({'X', 'f'})
for i in sets:
    # sets[i] = 'A'
    print("The new set value is {}".format(i))

print("""Dictionaries are perl hashes
represented with {}
command separated key value pairs
colon separated key and value
""")

dct = {'a': 1, 'b': 2, 'c': '3'}
for k, v in enumerate(dct):
    print("K => {} V => {}".format(k, v))

for i in dct.keys():
    print("K=>{} V=>{}".format(i, dct[i]))

print("Dict element {} is {}".format('a', dct['a']))
print("Values =>", dct.values())
print("Keys   =>", dct.keys())

for i, v in enumerate(dct):
    print("K->{} : V->{}".format(i, v))

print("------------------------------------")
