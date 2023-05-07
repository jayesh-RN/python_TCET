mytuple = ("Prashant", "Kumar", "Singh")
print(mytuple)
print(type(mytuple))
# requirement jab fix hogi...
# immutable

myset = {1, 2, "sanjay", 5.66}
print(myset)
myset.add(60)
print(myset)
myset.discard(60)
print(myset)
myset.remove(2)
# sure then use remove or else discard
print(myset)
urset = {"prashant", "sanjay", "kartik", "rishabh"}
newset = myset.union(urset)
print(newset)
print(myset.intersection(urset))
print(myset.difference(urset))
fs = frozenset(myset)  # immutable
print(fs)
print(type(fs))

mydic = {"name": "prashant", "age": 22,
         "marks": 99, "sex": "22"}
print(mydic)
mydic["name"] = "kartik"
a = mydic["name"]
print(a)


x = 10
y = 10
print(x is y)  # identity operator

name = "prashant"
print('z' in name)  # membership operator

# a = int(input("Enter a number: "))
# if(a > 0):
#     print("Positive")
# if(a < 0):
#     print("Negative")
# if(a == 0):
#     print("Zero")

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# max = 0
# min = 0
# if (a > b):
#     max = a
#     min = b
# if(b > a):
#     max = b
#     min = a
# c = int(input("Enter a number: "))
# if(c > max):
#     max = c
# if(c < min):
#     min = c
# d = int(input("Enter a number: "))
# if(d > max):
#     max = d
# if(d < min):
#     min = d
# e = int(input("Enter a number: "))
# if(e > max):
#     max = e
# if(e < min):
#     min = e
# print(max)
# print(min)
'''
p1 = int(input("Enter a p1: "))
p2 = int(input("Enter a p2: "))
p3 = int(input("Enter a p3: "))
p4 = int(input("Enter a p4: "))
p5 = int(input("Enter a p5: "))
prac1 = int(input("Enter a prac1: "))
prac2 = int(input("Enter a prac2: "))

if(p1 >= 40 and p2 >= 40 and p3 >= 40 and p4 >= 40 and p5 >= 40 and prac1 >= 10 and prac2 >= 10):
    print("Pass")
else:
    print("Fail")

total = p1+p2+p3+p4+p5
percentage = total/5.0
print("Total  = ", total)
print("Percentage = ", percentage)
'''


# ch = str(input("Enter a character: "))
# if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
#     print("Vowel")
# else:
#     print("Consonant")


# if ord(ch) >= 65 and ord(ch) <= 90:
#     print("Capital")
# elif ord(ch) >= 97 and ord(ch) <= 122:
#     print("Small")
# else:
#     print("Special Character")

for i in range(1, 11):
    print(i*2, " ", i*3, " ", i*4, " ", i*5, " ", i *
          6, " ", i*7, " ", i*8, " ", i*9, " ", i*10)

print("--------------------------------------")

for i in range(11, 21):
    print(i*2, " ", i*3, " ", i*4, " ", i*5, " ", i *
          6, " ", i*7, " ", i*8, " ", i*9, " ", i*10)
