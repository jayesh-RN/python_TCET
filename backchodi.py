import csv

f = open("waiter_name.csv", "a", newline="")
a = csv.writer(f)
a.writerow(["waiter_name"])
table_name = input("waiter ka naam ")
a.writerow([table_name])