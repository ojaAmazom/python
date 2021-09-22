f = open('16_2_read.txt')

Line1 = f.readline()
Line2 = f.readline()
Line3 = f.readline()

print(Line1, end='')
print(Line2, end='')
print(Line3, end='')

f.close()