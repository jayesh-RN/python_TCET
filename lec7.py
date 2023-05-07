# class New:
#     self.a = 10

#     def __init__(self):
#         self.name = "prashant"


# obj1 = New()
# obj2 = New()
# obj3 = New()


# class college:
#     collegename = "xyz"
# # static variable

#     def __init__(self):
#         self.studentname = "prashant"


# principal = college()
# teacher = college()
# accountant = college()

# print("principal.collegename = ", principal.collegename,
#       "--->", "principal.studentname = ", principal.studentname)
# print("teacher.collegename = ", teacher.collegename,
#       "--->", "teacher.studentname = ", teacher.studentname)
# print("accountant.collegename = ", accountant.collegename,
#       "--->", "accountant.studentname = ", accountant.studentname)

# college.collegename = "abc"
# # second way to add static variable
# principal.studentname = "jha"

# print("principal.collegename = ", principal.collegename,
#       "--->", "principal.studentname = ", principal.studentname)
# print("teacher.collegename = ", teacher.collegename,
#       "--->", "teacher.studentname = ", teacher.studentname)
# print("accountant.collegename = ", accountant.collegename,
#       "--->", "accountant.studentname = ", accountant.studentname)


# print("............................................")


# class Student:
#     # by using class anme we can access static method
#     @staticmethod
#     def get_personal_detail(f_name, l_name):
#         print("FirstName = ", f_name, "LastName = ", l_name)

#     @staticmethod
#     def contact_detail(mobil_no, rollno):
#         print("Mobile No = ", mobil_no, "Roll No = ", rollno)


# # static method isko obj se lena dena nahi hai
# Student.get_personal_detail("prashant", "jha")
# Student.contact_detail(1234567890, 101)


# print("............................................")


# # inheritance
# # Syntax
# # class derived-class(base-class(parent class)):

# class College:
#     def college_name(self):
#         print("College Name = XYZ")


# class Student(College):
#     def student_info(self):
#         print("Student Name = Prashant")
#         print("branch = CS")


# obj = Student()
# obj.college_name()
# obj.student_info()


# print("............................................")


# class SubjMarks:
#     math = int(input("Enter Math Marks: "))
#     de = int(input("Enter DE Marks: "))
#     c = int(input("Enter C Marks: "))
#     english = int(input("Enter English Marks: "))


# class PractMarks:
#     cpract = int(input("Enter CPract Marks: "))


# class Result(SubjMarks, PractMarks):
#     def total(self):
#         if self.math >= 35 and self.de >= 35 and self.c >= 35 and self.english >= 35 and self.cpract >= 35:
#             print("pass")
#         else:
#             print("fail")


# obj = Result()
# obj.total()


print("............................................")


class Hospital:
    H_name = input("Enter Hospital Name: ")


class patient:
    P_name = input("Enter Patient Name: ")
    P_age = int(input("Enter Patient Age: "))
    P_medicine = input("Enter Patient Medicine: ")


class HospitalStaff:
    S_name = input("Enter Staff Name: ")
    S_age = int(input("Enter Staff Age: "))


class pharmacy(HospitalStaff, Hospital, patient):
    c_name = input("Enter Pharmacy Name: ")
    m_price = int(input("E"))

    def chemist(self):
        print("************Pharmacy Name is ", self.c_name, "****************")
        print("-----------Receipt-----------")
        print("Hospital Name = ", self.H_name)
        print("Patient Name = ", self.P_name)
        print("Patient Age = ", self.P_age)
        print("recomended by dostor = ", self.S_name)
        print("Patient Medicine = ", self.P_medicine,
              "       ------->>>    price =  ", self.m_price)


obj = pharmacy()
obj.chemist()
