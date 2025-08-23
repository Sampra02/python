A = int(input("enter A :" ))
sum = 0
for i in range(1,A):
    if(i%2!=0):
        sum = sum+i
        continue
    print(sum)