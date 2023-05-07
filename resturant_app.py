import csv

while True:
    print("1. Admin    ,  2. User  ,  3. Exit")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        while True:
            print("1. Add Food Item  ,  2. Add Table  ,  3. Add Waiter  ,  4. Exit")
            ch = int(input("Enter your choice: "))
            if(ch==1):
                f = open("resturant.csv", "a", newline="")
                a = csv.writer(f)
                # a.writerow(["food_name", "food_price"])
                food_name = input("kahne ka naam  ")
                food_price = int(input(" khane ka daam "))
                a.writerow([food_name,food_price])
            elif(ch==2):
                f = open("table.csv", "a", newline="")
                a = csv.writer(f)
                # a.writerow(["table_name"])
                table_name = input("table ka naam  ")
                a.writerow([table_name])
            elif(ch==3):
                f = open("waiter_name.csv", "a", newline="")
                a = csv.writer(f)
                # a.writerow(["waiter_name"])
                table_name = input("waiter ka naam ")
                a.writerow([table_name])
            elif(ch==4):
                break
    elif(choice==2):
        while True:
            print("1. Menu  ,  2. Table  ,  3. Waiter  ,  4. Exit")
            ch = int(input("Enter your choice: "))
            if(ch==1):
                f = open("resturant.csv", "r")
                a = csv.reader(f)
                for i in a:
                    print(i[0])
                    print(i[1])
            elif(ch==2):
                f = open("table.csv", "r")
                a = csv.reader(f)
                cnt = 0;
                for i in a:
                    cnt=i
                print(cnt);
            elif(ch==3):
                f = open("waiter_name.csv", "r")
                a = csv.reader(f)
                for i in a:
                    if(i==0):
                        continue
                    print(i)
            elif(ch==4):
                break                
    elif(choice==3):
        break           
    else:
        print("g*** mara phirse kare run") 
        break   
                    
                