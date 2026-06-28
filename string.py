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