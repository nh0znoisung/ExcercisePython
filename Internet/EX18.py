#Calculate a + aa + aaa + aaaa
# 1  +11 + 111+ 1111 = 1234

#Use function int("%s" % a)

a = input("Enter your number:   ")

n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
n4 = int("%s%s%s%s" % (a,a,a,a))

print("The format value is: ", n1+n2+n3+n4)