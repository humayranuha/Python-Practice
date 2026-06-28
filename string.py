# multiline string
string = """don't know what to type,
            excited for today's match"""

print(string)

# loop through
for c in string:
    print(c)

# checking for existence of certain phrase
if "type" in string:
    print("'type' in string")

if "tom" not in string:
    print("'tom' not in string")

#slicing
print(string[2:5])
print(string[:5])
print(string[2:])
print(string[-5: -2])

# several methods
b = "Hello, Python!!!"
print(b.upper())
print(b.lower())
print(b.strip())
print(b.replace("H", "N"))
print(b.split(","))