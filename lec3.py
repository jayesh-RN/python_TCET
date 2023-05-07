# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)


# n = 6
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i, " ", n-i, " ")


# for i, j in zip(range(1, 6), range(5, 0, -1)):
#     if i == 3 and j == 3:
#         continue
#     print(i, " ", j)
# //when range not known use while loop

# while(True):
#     i = int(input("Enter your choice: "))
#     if(i == 1):
#         j = int(input("Enter a number: "))
#         k = int(input("Enter a number: "))
#         print(j+k)
#     elif(i == 2):
#         j = int(input("Enter a number: "))
#         k = int(input("Enter a number: "))
#         print(j-k)
#     elif(i == 3):
#         j = int(input("Enter a number: "))
#         k = int(input("Enter a number: "))
#         print(j*k)
#     elif(i == 4):
#         j = int(input("Enter a number: "))
#         k = int(input("Enter a number: "))
#         print(j/k)
#     print("Do you want to continue? (y/n)")
#     ch = input()
#     if(ch == 'n'):
#         break


# def info(firstname, lastname, age):
#     print("First Name: ", firstname)
#     print("Last Name: ", lastname)
#     print("Age: ", age)


# info('pranav', 'kumar', 20)


# def add(num1, num2):
#     return num1+num2


# results = add(10, 20)


# def arithematic(a, b):
#     r = a+b
#     n = a*b
#     m = a-b
#     return r, n, m


# result = arithematic(10, 20)
# print("Result: ", result)


# def func(city="Delhi"):
#     print("City: ", city)


# func("Nagpur")
# func()


# def name(*name):
#     print(name)


# name("pranav", "kumar", "singh", 1001)

# x = 0


# def info_one():
#     x = 17
#     # local
#     print("X=", x)


# def info_two():
#     print("X=", x)


# info_one()
# info_two()


# u = Jayesh
# p = 1234


# def result():
#     while True:
#         username = input("Enter your username: ")
#         if username == u and password == p:
#             print("Welcome")
#             break
#         else:
#             print("Invalid username or password")

#     collegeName = input("Enter your college name: ")
#     year = int(input("Enter your year: "))
#     rollNo = int(input("Enter your roll no: "))
#     collegeName = str(input("Enter your collegename :"))

import csv
f = open("students.csv", "a", newline="")
a = csv.writer(f)
a.writerow(["studentID", "rollno", "name", "mobile", "p1", "p2",
           "p3", "p4", "p5", "total", "percentage", "grade"])
n = int(input("Enter the number of students: "))
while(n > 0):
    n = n-1
    studentID = int(input("Enter your studentID"))
    rollno = int(input("Enter your rollno"))
    name = input("Enter your name")
    mobile = int(input("Enter your mobile"))
    email = input("Enter your email")
    p1 = int(input("Enter your p1"))
    p2 = int(input("Enter your p2"))
    p3 = int(input("Enter your p3"))
    p4 = int(input("Enter your p4"))
    p5 = int(input("Enter your p5"))
    total = p1+p2+p3+p4+p5
    if(p1 >= 35 and p2 >= 35 and p3 >= 35 and p4 >= 35 and p5 >= 35):
        grade = "pass"
    else:
        grade = "fail"
    a.writerow([studentID, rollno, name, mobile, email,
                p1, p2, p3, p4, p5, total, grade])
    print("student data is added successfully")
