# list is a collection which is ordered and changeable. Allows duplicate members. 
list1 = ["apple", "banana", "cherry"]
list2 = list(("apple", "banana")) # double round-brackets
list3 = ["apple", "banana", "cherry", "apple"] # duplicate values allowed
tropical = ["mango", "jackfruit"]
print(list1)
print(type(list2))
print(len(list3))

# Accessing list items
print(list1[0])
print(list1[-1])
print(list3[1:3])
print(list3[-3:-1])

# Changing list items
list3[3:4] = ["watermelon"]
print(list3)
list3.insert(4, "lichi")
print(list3)

# Adding items to the list
list3.append("orange")
print(list3)
list3.extend(tropical)
print(list3)

# Removing an item
# list3.remove("banana") # for duplicate values, it removes the first occurrence
# print(list3)
# list3.pop() # last item gets removed, indexes can be used to remove any item
# print(list3)
# del list3[2]
# print(list3)
# list2.clear() # clears the list but list remains
# print(list3)

# List comprehension
# newlist = [expression for item in iterable if condition == True]
newList = [x for x in list3 if x != "apple"]
print("New List: ", newList)

# List sorting
newList.sort()
print(newList)
newList.sort(reverse=True) # descending sorting
print(newList)
numbers = [100, 50, 23, 65]
def myFunc(n):
    return abs(n - 50)

numbers.sort(key=myFunc)
print(numbers)

newList.sort(key=str.lower)
print(newList)

# Copying lists
colors1 = ["blue", "green", "purple"]
colors2 = colors1.copy()
print(colors2)
colors3 = list(colors2)
print(colors3)
colors4 = colors3[:] # slicing
print(colors4)


