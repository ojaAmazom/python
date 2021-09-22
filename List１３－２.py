f = open('Hello.txt')

Line1 = f.readline()
Line2 = f.readline()

print(Line1, end='')
print(Line2, end='')

f.close()