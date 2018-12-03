#Sanjay Bajnath
#Python Task - List Management

user_input= input("Enter a list of numbers, separated by commas.")
check_num = input("What number are you looking for in this list?")
user_input = user_input.replace(" ","")
number_list =user_input.split(",")

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
print("avg = ",(list_sum/len(number_list)))


    



    
