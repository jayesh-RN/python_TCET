'''
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held			-		7856
Number of classes attended.		-		856			80%
And print
percentage of class attended
Is student is allowed to sit in exam or not.

'''

total = int(input("Enter no. of class held: "))
attended = int(input("Enter no. of class attended: "))
percent = (attended/total)*100
print("Your attendance is: ",percent)

if percent>=75:
    print("You are allowed to sit in exam")
else:
    print("You are not allowed to sit in exam")