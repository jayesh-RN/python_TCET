import csv
# f = open("myfile.txt", "w")
# print("name of file", f.name)
# print("mode of file", f.mode)
# print("readable or not", f.readable())
# print("writable or not", f.writable())
# print("closed or not", f.closed)
# f.close()
# print("closed or not", f.closed)


# f = open("covid.txt", "w")
# mylist = ["NGP is full vaccinated city", "NGP is full vaccinated city",
#           "NGP is full vaccinated city", "NGP is full vaccinated city", "NGP is full vaccinated city"]
# f.writelines(mylist)
# float
# f.close()
# print("file operation done")


# with open("myfile.txt", "w") as f:
#     f.write("amit\n")
#     f.write("amita\n")
#     f.write("amitb\n")
#     print("file closed :", f.closed)

# print("file closed :", f.closed)


f = open("student.csv", "a", newline="")
a = csv.writer(f)
a.writerow(["studentID", "name", "age", "marks"])
studentid = int(input("Enter a studentid: "))
rollno = int(input("Enter a rollno: "))
age = int(input("Enter a age: "))
marks = int(input("Enter a marks: "))
a.writerow([studentid, rollno, age, marks])

# f1 = open("Guido.jpg", "rb")
# f2 = open("Rossom.jpg", "wb")
# data = f1.read()
# f2.write(data)
