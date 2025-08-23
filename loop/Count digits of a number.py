n = int(input("enter number :" ))
count = 0
temp = n
while temp>0:
    count+=1
    temp//=10
print("number of digits:",count)
