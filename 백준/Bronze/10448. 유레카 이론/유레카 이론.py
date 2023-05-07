import sys
ans =[0]*1001
l = [n*(n+1)//2 for n in range(1, 45)]
for i in l:
    for j in l:
        for k in l:
            if i+j+k <= 1000:
                ans[i+j+k] = 1
n = int(input())
for _ in range(n):
    print(ans[int(input())])