N=int(input("enter a number"))
for i in range(1,N+1):
    for j in range(1,N+2):
        if(j==1)or(j==N):
            print("*",end="")
        else:
            print("*",end="")
    print()