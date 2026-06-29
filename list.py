# list is a collection which is ordered and changeable. Allows duplicate members. 
list1 = ["apple", "banana", "cherry"]
list2 = list(("apple", "banana")) # double round-brackets
list3 = ["apple", "banana", "cherry", "apple"] # duplicate values allowed
print(list1)
print(type(list2))
print(len(list3))

# Accessing list items
print(list1[0])
print(list1[-1])
print(list3[1:3])
print(list3[-3:-1])

