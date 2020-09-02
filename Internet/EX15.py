#in range 1000 -> 3000
def checkEvenChar(n):
  while n > 0:
    if n % 2 == 1 :
      return False
    n = n/10
  return True

vals = []

for i in range(1000, 3001):
  if(checkEvenChar(i)):
    vals.append(str(i))

print(",".join(vals))



