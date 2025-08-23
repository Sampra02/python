a=int(input("enter right angle:"))
b=int(input("enter obtuse angle:"))
c=int(input("enter acute angle:"))
if a+b+c==180:
    if 90 in (a, b, c):
        print("Right Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Not a valid triangle")