# calculate the number of characters, numbers

s = input("Enter your string: \n")

char = 0
num = 0
for i in s:
  if i >= "a" and i<="z" or i >= "A" and i <="Z":
    char += 1
  elif i>="0" and i<= "9" :
    num += 1

print("Number of character: " , char)
print("Number of number: " , num)
    

