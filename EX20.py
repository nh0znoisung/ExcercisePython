'''
Have the 
D 100
W 200
D= send, W= use
'''
money = 0

while True:
  s = input().spilt()
  if s:
    if s[0] == 'D':
      money += int(s[1])
    if s[0] == 'W':
      money -= int(s[1])
  else:
    break

print(money)