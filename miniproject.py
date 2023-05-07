# New Program:
import csv


def create():
    f = open("student.csv", "a", newline="")
    a = csv.writer(f)
    a.writerow(["studentId", "name", "roll no", "email id", "address", "mobileno",
               "p1", "p2", "p3", "p4", "p5", "total", "percentage", "Result"])
    try:
        records = int(input("Enter no of records"))
    except ValueError as message:
        print(message)
    else:
        while records > 0:
            records = records-1
            try:
                studentId = int(input("Enter your student id: "))
                name = input("Enter name: ")
                rollno = int(input("Enter rollno: "))
                email = input("Enter email: ")
                address = input("Enter address: ")
                mobileno = input("Enter mobile no: ")
                p1 = int(input("Enter marks in p1:     "))
                p2 = int(input("Enter marks in p2:     "))
                p3 = int(input("Enter marks in p3:     "))
                p4 = int(input("Enter marks in p4:     "))
                p5 = int(input("Enter marks in p5:     "))
            except ValueError as message:
                print(message, "ReRun the program")
                break
            total = p1+p2+p3+p4+p5
            percentage = total/5.0
            if p1 < 40 or p2 < 40 or p3 < 40 or p4 < 40 or p5 < 40:
                result = "fail"
            else:
                result = "pass"
            a.writerow([studentId, name, rollno, email, address,
                        mobileno, p1, p2, p3, p4, p5, total, percentage, result])

        print("student data has saved")


def readRecord():
    with open("student.csv") as f:
        f = open("student.csv", "r")
        a = csv.reader(f)
        try:
            id = int(input("Enter id to display: "))
        except ValueError as message:
            print(message, "rerun the program")
            return
        else:
            flag = False
            for i in a:
                if i[0] == str(id):
                    print(i)
                    Flag = True
            if Flag == False:
                print("No such id found")


while(True):
    try:
        choice = int(
            input("Enter your choice: 1. Enter student data, 2. Read Student record , 3.Exit    "))
        if choice == 1:
            create()
        if choice == 2:
            readRecord()
        if choice == 3:
            break
    except ValueError:
        print("put appropriate value")
