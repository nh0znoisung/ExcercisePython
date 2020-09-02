#USe function isalpha, isdigit to check

s = input("Enter your string: \n")

# d = {}
d = {"digit": 0, "character": 0}

for i in s:
  if i.isdigit():
    d["digit"] += 1
  if i.isalpha():
    d["character"] += 1
  else:
    pass

print("Number of character: ", d["character"])
print("Number of digit: ", d["digit"])