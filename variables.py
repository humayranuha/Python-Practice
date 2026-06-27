a = 50
a = "Sally"

# type casting
x = str(3)
y = int(5)
z = float(1)

print(a, x, y, z)
print(type(a), type(x), type(y), type(z))

# assigning values to multiple variables
p, q, r = "psg", "quinton", "rial"

# assigning same value to multiple variables
t = u = v = "orange"

print(p, q, r)
print(t, u, v)

# unpack a collection
colors = ["yellow", "skyblue", "red"]
e, f, g = colors
print(e, f, g)

# global variable case
n = "awesome"
m = "java"

def myFunc():
    n = "fantastic"
    global m 
    m = "python"

    print("Python is", n)

myFunc()
    
print("Python is", n)
print("I love", m)