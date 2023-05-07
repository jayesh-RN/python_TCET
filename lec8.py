# # how to acheive polymorphism

# # compile time polymorphism
# #
# # overridding se runtime poly

# # function overloading

# # class Principal:
# #     def role(self):
# #         print("i am managing all activity")


# # class Deasn:
# #     def role(self):
# #         print("i am Dean principal ka baap")


# # class Hod:
# #     def role(self):
# #         print("i am managing teacher and student")


# # class Faculty:
# #     def role(self):
# #         print("i am completing syllabus")


# # def func(obj):
# #     obj.role()


# # eak naam ka bht function
# # print("-------------")
# # campus = [Principal(), Deasn(), Hod(), Faculty()]
# # for obj in campus:
# #     func(obj)


# # class Deposit:
# #     def __init__(self, cash):
# #         self.cash = cash
# # # operatoer overloading

# #     def __add__(self, other):
# #         return self.cash + other.cash


# # d1 = Deposit(1000)
# # d2 = Deposit(2000)
# # print(d1+d2)

# # + se magic metjod hojata hai overwrite
# # internlly implemented

# # method overloading is not supported
# # if we are trying to declare multiple methods with same name ans different number of arguments ten oython will always consider only last method


# # class Arithmetic:
# #     def add(self, a):
# #         print(a)

# #     def add(self, a, b):
# #         print(a+b)

# #     def add(self, a, b, c):
# #         print(a+b+c)


# # obj = Arithmetic()
# # # obj.add(10)
# # # obj.add(10, 20)
# # obj.add(1, 2, 3)


# # constructor overloading not supported same as methjod overloading
# # class Arithmetic:
# #     def __init__(self):
# #         print("There is no argument")

# #     def __init__(self, a):
# #         print("passing one argument")

# #     def __init__(self, a, b):
# #         print("passing two argument")


# # obj = Arithmetic()
# # obj = Arithmetic(10)
# # obj = Arithmetic(2, 2)


# # method overriding
# class Father:
#     def bike(self):
#         print("harley Davidson")

#     def laptop(self):
#         print("laptop with 2gb ram and 5000 gb HDD I3 processor")


# class Aman(Father):
#     def laptop(self):
#         print("As prer my programming mac")
#     super().laptop()


# obj = Aman()
# obj.bike()
# obj.laptop()


# class Father:
#     def __init__(self):
#         print("im in the office")
# class child(Father):
#     def __init__(self):
#         print("I am in my class")
#         super().__init__()


choice = 0


class Exam(object):
    def __init__(self):
        self.sname = None
        self.classname = None
        self.rollno = 0
        self.collegename = None
        self.login()

    def login(self):
        print("=============================")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("=============================")
        print()
        # login sectiopn
        if username == password:
            print("Login Successfull")
            self.getdata()
        else:
            print("Login Failed")
    print("=======================================")

    def getdata(self):
        self.sname = input("Enter your name: ")
        self.classname = input("Enter your class: ")
        self.rollno = int(input("Enter your rollno: "))
        self.collegename = input("Enter your college name: ")
        print()
        print("chose any branch for exam")
        print("1.mech")
        print("2.it")
        print("3.civil engineering")
        print("4.civil engineering")
        print()

        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.mechanical()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("Invalid choice")

    def mechanical(self):
        print("1. first semester")
        print("2. second semester")
        print("Enter your sem number")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("maths")
        elif choice == 2:
            pass

    def information(self):
        print("1. first semester")
        print("2. second semester")
        print("Enter your sem number")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("maths")
        elif choice == 2:
            pass

    def computer(self):
        print("1. first semester")
        print("2. second semester")
        print("Enter your sem number")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("maths")
        elif choice == 2:
            pass

    def civil(self):
        print("1. first semester")
        print("2. second semester")
        print("Enter your sem number")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("maths")
        elif choice == 2:
            pass

# obj = creation of class
# obj.exam()
# obj.login()


class Calculation(object):
    def __init__(self):
        self.start = 0
        self.dmgt = 0
        self.cg = 0
        self.toc = 0
        self.math = 0
        self.total = 0
        self.percentage = 0
        self.ps = 0
        print()
        print("Do you want to put Examination marks(y/n)")
        print()
        Yes = input("Enter your choice: ")
        if Yes == "y":
            self.calculatemarks()
        else:
            print("Thank you")
        print()

    def calculatemarks(self):
        self.stat = int(input("Enter your stat marks: "))
        self.dmgt = int(input("Enter your dmgt marks: "))
        self.cg = int(input("Enter your cg marks: "))
        self.toc = int(input("Enter your toc marks: "))
        self.math = int(input("Enter your math marks: "))
        print()

        if self.stat >= 40 and self.dmgt >= 40 and self.cg >= 40 and self.toc >= 40 and self.math >= 40:
            self.ps = "pass"
            print("you are pass")
        else:
            self.ps = "fail"
            print("you are fail")
        self.total = self.stat + self.dmgt + self.cg + self.toc + self.math
        self.percentage = self.total/5.0


# obj1 = Calculation()


class Assessment(Exam, Calculation):
    def __init__(self):
        Exam.__init__(self)
        Calculation.__init__(self)

    def result(self):
        print("=========================================================================================================================================================")
        print("                                                                                                                                                          ")
        print("                                                                       college name: ",
              self.collegename, "                                                 ")
        print("                                                                                                                                                           ")
        print("========================================================================================================================================================")
        print("                                                                                                                                                          ")
        print("                                                                       Student name: ",
              self.sname, "                                                      ")
        print("                                                                       Class Name: ",
              self.classname, "                                                      ")
        print("                                                                       Roll No: ",
              self.rollno, "                                                      ")
        print("                                                                                                                                                           ")
        print("========================================================================================================================================================")
        print("                         subject name          :            Totalmarks                         :           obtained marks :                            ")
        print("                                                                                                                                                          ")
        print("                         stat                  :            100                                :           ",
              self.stat, "                              ")
        print("                         dmgt                  :            100                                :           ",
              self.dmgt, "                              ")
        print("                         cg                    :            100                                :           ",
              self.cg, "                              ")
        print("                         toc                   :            100                                :           ",
              self.toc, "                              ")
        print("                         math                  :            100                                :           ",
              self.math, "                              ")
        print("========================================================================================================================================================")
        print("                                                                                                                                                          ")
        print("                         Result            :                                                 :           ",
              self.ps, "                                    ")
        print("                         Total marks           :            500                                :           ",
              "                                          ")
        print("                         obtained marks           :            500                                :         ",
              self.total, "                                          ")
        print("                         Percentage            :            100                                :           ",
              self.percentage, "                              ")
        print("========================================================================================================================================================")


obj2 = Assessment()
obj2.result()
