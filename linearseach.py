# def linearsearch(array, value):
#     for i in range(len(array)):
#         if array[i] == value:
#             return i
#     return -1


# def pair(array):
#     ans = 0;
#     for i in range(len(array)):
#         if(i==0):
#             continue
#         if array[i] == array[i-1]:
#             ans +=1
#     return ans

# array = [1,2,2,3,4,4,4,5,6,7,7]
# x = 2;

# print(linearsearch(array, x))
# print(pair(array))





res = "we dont need no education we dont need no thought control no we dont";
target = "dont";

array = [];

index = 0;
for i in range(len(res)):
    if(res[i] == " "):
        index += 1;
    
print(index)        







