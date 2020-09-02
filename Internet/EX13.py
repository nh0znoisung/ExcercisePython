# Input: is the string have and space, we need to eliminate the space, destroy the similar, sort it and print it respectively

s = input("Enter your string please: \n").split()

words = [word for word in s]
print (" ".join(sorted(list(set(words)))))
