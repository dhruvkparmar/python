# use the loop to find the factorial of a given number
num = int(input("Enter Number : "))

fact = 1

for i in range(num,0,-1):
    #find factorial
    fact *= i
else:
    print("Factorial of",num,"is : ",fact)
