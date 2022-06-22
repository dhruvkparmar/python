#Print the following pattern
"""
   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
   
"""
# first loop to add one row

for i in range(1,6):
    # secound loop to print number
    
    for j in range(1,i+1):
        print(j , end=" ")
    print()
