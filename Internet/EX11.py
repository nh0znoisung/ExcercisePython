a = input("Enter the two numbers: \n").split()
X = int(a[0])
Y = int(a[1])

multidim = [[0 for i in range(X)] for j in range(Y)]

for i in range(X):
  for j in range(Y):
    multidim[j][i] = i*j

print(multidim)