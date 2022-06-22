# Calculate the sum of all numbers from 1 to a given number

# input no 
num = int(input("Enter any number : "))

ans = 0
# add number in range 
for i in range(1,num+1):
    ans += i
    
# print ans 
print("sum of 1 to ",num," : ",ans)
