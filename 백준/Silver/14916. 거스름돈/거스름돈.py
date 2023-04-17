coin = int(input())  #거스름돈
res = 0  #동전 개수

while coin >= 0:
    if coin % 5 == 0:
        print(res + (coin // 5))
        break
    coin -= 2
    res += 1
else:  #거슬러줄 수 없으면
    print(-1)
