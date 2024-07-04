print("Hello world")

b,c,d=5,6.2,"Hello world"

print("{} {}".format("Value of",d))

print(type(b))

values=[1, 2.5, "Abhishek", 5, 6]
print(values)
#print[0]
print(values[2])
print(values[2:5])
values.insert(0, "Tiwari")
print(values)
values.append(9)
print(values)

values[2]="ABHISHEK"
print(values)
del values[6]
print(values)

# Dictionary data types
dic={'a': 5, 2:'Abhishek Tiwari', 'c': "Hello world"}
print(dic[2])
print(dic['a'])
print(dic['c'])


dict={}

dict["First name"] ="Abhishek"
dict["Last name"]="Tiwari"
dict["Gender"]="Male"
print(dict)

