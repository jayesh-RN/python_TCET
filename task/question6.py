# Take input of age of 3 people by user and determine oldest and youngest among them.

person1 = int(input("Enter age of person1: "))
person2 = int(input("Enter age of person2: "))
person3 = int(input("Enter age of person3: "))

if person1<0 or person2<0 or person3<0:
    print("Enter valid age")
elif person1>=person2 and person1>=person3:
    print("Person 1 is oldest")
elif person2>=person1 and person2>=person3:
    print("Person 2 is oldest")
elif person3>=person1 and person3>=person2:
    print("Person 3 is oldest")


if person1<=person2 and person1<=person3:
    print("Person 1 is youngest")
elif person2<=person1 and person2<=person3:
    print("Person 2 is youngest")
elif person3<=person1 and person3<=person2:
    print("Person 3 is youngest")
