#Sanjay Bajnath
#Python Task - List Management

user_input= input("Enter a list of numbers, separated by commas.")
check_num = input("What number are you looking for in this list?")
user_input = user_input.replace(" ","")
number_list =user_input.split(",")

print("There are",len(number_list)," numberes in this list.")

number_set = "{"
for i in range(0,len(number_list)-1):
    number_set= number_set + number_list[i]+","
number_set = number_set + number_list[len(number_list)-1]+"}"
print(number_set)

contains = False
num_count = 0
for i in range(0,len(number_list)):
    if(float(number_list[i])==float(check_num)):
        contains = True
        num_count +=1
if(contains):
    print(check_num," is on the list",num_count,"times.")
else:
    print(check_num,"is not in the list")

list_sum = 0
for i in range(0,len(number_list)):
    list_sum += float(number_list[i])
print("The average of the numbers in the list is ",(list_sum/len(number_list)))

for i in range(0,len(number_list)):
    number_list[i]=float(number_list[i])
    if(number_list[i] %1 == 0):
        number_list[i] = int(number_list[i])
print("The list in order is:",sorted(number_list))
median = 0
if(len(number_list)%2==1):
     median = number_list[int(len(number_list)/2)]
else:
    median = (number_list[int((len(number_list)-1)/2)]+number_list[int((len(number_list))/2)])/2

print("The median of the numbers in the list is: ",median)

    
