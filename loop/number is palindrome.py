A = int(input("Enter A: "))
reversed = 0
temp = A
while temp > 0:
    reversed = reversed * 10 + temp % 10
    temp //= 10
if A == reversed:
    print("it is palindrome")
else:
    print("it is not Palindrome")