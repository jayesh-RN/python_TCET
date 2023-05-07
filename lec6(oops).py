class New:
    x = 10

    def display(self):
        print("hello python")
# python class having default constructor
# by using conytructor we can initialize the instance variable
# constructor is a special method which is used to initialize the instance variable


obj = New()
obj.display()
print(obj.x)
# print(obj.a)

print("............................................")


class NewClass:
    def __init__(self):
        print("my name is contructor and i will allways call when object is created an d executed first")

    def show(self):
        print("welcome to classs level programming")


obj = NewClass()
obj.show()
obj2 = NewClass()


print("............................................")


class Hod:
    def __init__(self):
        self.name = 'sonali'
        self.age = 21
        self.empid = 101

    def info(self):
        print("name is", self.name)
        print("age is", self.age)
        print("empid is", self.empid)


obj = Hod()
obj.info()
# how many types of variablewe can declare
# instance variable static variable and local variable
# types of method
# class method static method and instance method


print("............................................")


# declaring instance variable inside a constructor by using self variable
# class student:
#     def __init__(self):
#         self.s_name = "prashant"
#         self.l_name = "jha"
#         self.s_rollno = 101
#         self.s_branch = "cs"
#         self.s_mb = 0000000000


# obj = student()
# print(obj.__dict__)


print("............................................")


# declaring instance variable inside a instance method by using self variable


class student:
    def __init__(self):
        self.s_name = "prashant"
        self.l_name = "jha"
        self.s_rollno = 101
        self.s_branch = "cs"

    def getdata(self):
        # instance method
        self.s_mb = 2888565454


obj = student()
obj.getdata()
print(obj.__dict__)


print("............................................")


class student:
    def __init__(self):
        self.s_name = "prashant"
        self.l_name = "jha"
        self.s_rollno = 101
        # self.s_branch = "cs"

    def getdata(self):
        # instance method
        self.s_mb = 2888565454


obj = student()
obj.getdata()
obj.s_branch = "it"
print(obj.__dict__)


print("............................................")


class student:
    def __init__(self):
        self.s_name = "prashant"
        self.l_name = "jha"
        self.s_rollno = 101
        # self.s_branch = "cs"

    def getdata(self):
        # instance method
        self.s_mb = 2888565454


obj = student()
obj.getdata()
obj.s_branch = "it"
del obj.s_rollno
print(obj.s_name)
print(obj.__dict__)


# satatic variable
# static variable is a variable which is common for all the object of a class


