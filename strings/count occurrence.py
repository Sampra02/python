a="abobc"
count=0
for i in range(0,len(a)):
    if a[i]=='b' and a[i+1]=='o' and a[i+2]=='b':
        print(a[i],a[i+1],a[i+2])
        count=count+1
print(count)