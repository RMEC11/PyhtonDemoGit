file = open('test.txt')
#print(file.read(3))
#print(file.read())

#line = file.readline()

#while line != "":
 #   print(line)
   # line = file.readline()
for line in file.readlines():
       print(line)

file.close()
