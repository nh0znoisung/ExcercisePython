#Count the isLower and isUpper()

s = input("Enter the string: \n")

Upper = 0
Lower = 0

for i in s:
  if i.isupper():
    Upper += 1
  if i.islower():
    Lower += 1

print("Number of Upper character: ", Upper)
print("Number of Lower character: ", Lower)

