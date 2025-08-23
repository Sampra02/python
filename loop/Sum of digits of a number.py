num = int(input("enter"))
sum = 0
while num>0:
    digit =num%10
    sum+=digit
    num//=10
print("sum of digits:",sum)