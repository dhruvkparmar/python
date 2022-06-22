"""
    calculate the sum of series up to n term. For example, if n =5 the
series will become 2 + 22 + 222 + 2222 + 22222 = 24690
"""
num = int(input("Enter Number : "))

temp = 2
ans = 0
for i in range(1,num+1):
    for j in range(1,i+1):
        if j==1:
            temp = 2
        else:
            temp = (temp*10)+2
    else:
        ans = ans + temp

print(ans)
