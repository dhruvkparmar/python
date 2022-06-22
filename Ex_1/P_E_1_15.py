"""
 elements from a given list present at odd index positions
    Given: my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    Expected output: 20 40 60 80 100
"""
lst = [10,20,30,40,50,60,70,80,90,100]

for i in range(1,11):
    if i%2==0:
        print(lst[i-1],end=" ")
