"""
    display only those numbers from a list that satisfy the following conditions
"""
"""
 * conditions
    - The number must be divisible by five
    - If the number is greater than 150, then skip it and move to the next number
    - If the number is greater than 500, then stop the loop
"""
# list of number 
num = [12,75,150,180,145,525,50]

for i in num:
    if i>= 500:
        break
    else:
        if i%5==0:
            if i>150:
                continue
            else:
                print (i)
                
