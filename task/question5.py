'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

'''

marks = int(input("Enter your marks: "))
if(marks<25):
    print("Grade: F")
elif(25<=marks<45):
    print("Grade: E")
elif(45<=marks<50):
    print("Grade: D")
elif(50<=marks<60):
    print("Grade: C")
elif(60<=marks<80):
    print("Grade: B")
elif(marks>80):
    print("Grade: A")
else:
    print("Enter valid marks! ")
