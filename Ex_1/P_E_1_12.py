# Display Fibonacci series up to 10 terms

febo= 0
nextno = 1

for i in range(1,11):
    print(febo,end=" ")
    temp = febo + nextno
    febo = nextno
    nextno = temp
