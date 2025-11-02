s = input().split()
ans = []
for w in s:
    ans.append(w[::-1])
print(" ".join(ans))
