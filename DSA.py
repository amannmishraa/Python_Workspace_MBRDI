numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

myList=[10,"apple",12,13,14]
print("--------")
print(myList)
print(myList[1:2])
print(myList[1:3])
print(myList[:2])
print(myList[2:])

items=["apple","banana","cherry","orange","kiwi","melon","mango"]
if "apple" in items:
    print("Yes, 'apple' is in the fruits list")
elif "banana" in items:
    print("Yes, 'banana' is in the fruits list")
else:
    print("fruit not found")

for x in items:
    print(x)# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

'''--------------------------------------------------------------------'''


# If apple the print apple is rs.100/kg
# ---------------------
# Defining the Tuple
myTuple = ("Apple", 10, "Orange", "Grapes", 20.0, 10)

# 1. Accessing by index (index 3 is the 4th item)
print(myTuple[3])        # Output: Grapes

# 2. Accessing the last item using negative indexing
print(myTuple[-1])       # Output: 10

# 3. Slicing from index 2 up to (but not including) index 4
print(myTuple[2:4])      # Output: ('Orange', 'Grapes')

# 4. Slicing from the beginning up to index 4
print(myTuple[:4])       # Output: ('Apple', 10, 'Orange', 'Grapes')

# 5. Slicing from index 2 to the end
print(myTuple[2:])       # Output: ('Orange', 'Grapes', 20.0, 10)

# 6. Slicing with negative indices
print(myTuple[-4:-1])    # Output: ('Orange', 'Grapes', 20.0)

sensor_readings = ("2026-01-16", 22.5, "Sunny", 1013.2, 45, "North", "Active")

unique = {1, 2, 2, 3}
unique.add(4)
print(unique)

# Force-assign the new values
mySet1 = {"Apple", 10, "Orange", "Grapes", 20.0}
mySet2 = {30.0, 10, "Orange", "Apple", 40}

# Print the results
print("Union:", mySet1 | mySet2)
print("Intersection:", mySet1 & mySet2)
print("Difference:", mySet1 - mySet2)
print("Symmetric Difference:", mySet1 ^ mySet2)
'----------------------------------------------------------------'
employees_mon = {"Alice", "Bob", "Charlie"}
employees_tue = {"Bob", "Charlie", "David"}
# --------------------
# Define the Dictionary
myFriends = {"Sandy": 25, "John": 20, "Jane": 22}

# Accessing components
print(myFriends.items())   # View all pairs
print(myFriends.keys())    # View all names
print(myFriends.values())  # View all ages
print(myFriends["Sandy"])  # Get Sandy's age -> 25

# Updating values
myFriends["Sandy"] = 30    # Change age to 30
print(myFriends.items())

myFriends.update({"Sandy": 40}) # Update method
print(myFriends.items())

# Removing items
myFriends.pop("Sandy")     # Removes Sandy specifically
print(myFriends.items())

myFriends.popitem()        # Removes the last inserted item
print(myFriends.items())

del myFriends["John"]      # Another way to delete a specific key
print(myFriends.items())

information = {"name": "Alice",
               "age": 28,
               "address": {"home": {"street": "123 Main St","city": "Wonderland","zip": "12345"},
                           "work": {"street": "456 Work Rd","city": "Worktown","zip": "67890"},
                           "natives":{ "street": "456 Work Rd","city": "Worktown","zip": "67890"}},
               "hobbies": ["reading", "traveling", "swimming"]}

print(information["name"])  
print(information["address"]["city"])
print(information["hobbies"][1])