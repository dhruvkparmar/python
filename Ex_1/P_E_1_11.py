# display all prime numbers within a range
start = int(input("Enter Starting Value : "))
end = int(input("Enter Ending Value : "))

for n in range(start,end+1):
    for i in range(2,n):
        # it is not prime number 
        if n%i==0:
            break
        # it is prime number
    else:
        print(n)
