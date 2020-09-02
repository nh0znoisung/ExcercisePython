#check the number in the input is odd

s = input("Enter your number: \n").split(",")

vals = [x for x in s if int(x)%2 == 1]

print(",".join(vals))
  
