#Input is the string of the binary number with 4 character, we need to covert it to decimal number and check if they divide with 5.
#Use function int(num , 2) to change the binary number

s = input("Enter the sequence the binary number, Please: \n").split(",")

ans = []

for i in s:
  sum = int(i , base = 2)
  
  #Convert it to decimal
  if sum % 5 == 0:
    ans.append(i)
    print(sum)

print(ans) 