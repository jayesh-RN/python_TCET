# p1 = 50
# per = 60.5
# name = "John"
# pass1 = True
# print(type(p1))
# print(type(per))
# print(type(name))


# p1 = 50
# p2 = 60
# p3 = 70
# total = p1+p2+p3
# per = total/3
# print(per)


# name = "prashant"
# print(name[0])
# print(name[0:12:2])
# print(name[:5])
# print(name[:])


math = 50
phy = 50
chem = 50
hindi = 45
print(id(math))
print(id(phy))
print(id(chem))
print(id(hindi))
math = 69
print(id(math))


# alwats take input int string type
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(a+b)


print(int("4"))
print(float("4"))
# # in int
# print(int(3.14))
# #print(int(10+5j))
# print(int(True)) #=1
# print(int(False)) #=0
# #print(int("4.22"))
# print(int("4"))
# # print(int("Kartik")) #name cannot be changed

# in float
print(float(3))
# print(float(50+2j))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))
# print(float("name"))
print(complex(5, -3))
print(bool(0+0j))


mylist = ["prashant", "Aashish", "Rahul", "Rajesh", 77]
print(mylist)
mylist = ["Kartik", "Rishabh", "Mehul", 66,
          "Dolly", 20.56, True, "Roshan", False, "Jayesh"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])  # n=5,n-1=4
print(mylist[1:])  # n=5,n-1=4
print(mylist[1:8:2])  # n=8,n-1=7
print(mylist[5:9:3])
mylist.append("Rahul")
print(mylist)
mylist.remove("Rahul")
newlist = mylist.copy()


# # Nested list
# mylist = [['prashant', 'jha'], ['85.56'], [440022, "yyy"]]
# print("example of multidimensional list: ")
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0]) # prashant
# print(mylist[0][1]) # jha
# print(mylist[1][0]) # 85.56
# print(mylist[2][0]) # 440022
# print(mylist[2][1]) # yyy
