# print the following start pattern using the for loop
"""
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
"""
num = int (input ("enter number : "))

#print first part

for i in range(1,num):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
# print secounf part 
for i in range(1,num-1):
    for j in range(num-1,i,-1):
        print("*",end=" ")
    print()
