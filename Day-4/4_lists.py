# Lists - it's a data structure store items with different data types in ordered way enclosed within square brackets.
# It is mutable i.e we can modify it.

fruits = ["Apple", "Pear", "Cherry", "Orange", "Grapes"]

# Accessing items from list
print(fruits[0])
print(fruits[-1])

# Modifying list items
fruits[1] = "Banana"
print(fruits)

# Adding elements to the list
fruits.append("Pear")
print(fruits)

fruits.extend(["circle", "square", "rectangle"])
print(fruits)

# Insert "kiwi" at index 1
fruits.insert(1, "kiwi")
print(fruits)

# Remove or delete an item
fruits.remove("Banana")
print(fruits)

# remove an item from a specified index
fruits.pop(0)    # delete item from 0th index
print(fruits) 

# delete all elements
fruits.clear()        # or del fruits[:]
print(fruits)