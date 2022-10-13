'''
10 5
3
1 4
3 2
2 8
2 3
'''
import sys; sys.stdin = open('경비원.txt')
# 1 : 북 2 : 남 3 : 서 4 : 동
garo, sero = map(int, input().split())
N = int(input())
pos = [0] * (N+1)
# 동 서 남 북 4 3 2 1
D = [0] * sero
S = [0] * sero
N = [0] * garo
B = [0] * garo

dir = [0]
for i in range(1, N+1):
    d, x = map(int, input().split())
    dir.append(d)
    if d == 1:
        pos[i] = [sero, x]
    elif d == 2:
        pos[i] = [0, x]
    elif d == 3:
        pos[i] = [sero - x, 0]
    elif d == 4:
        pos[i] = [sero-x, garo]
dd, xx = map(int,input().split())
total = 0
if d == 1:  # 북쪽
    s,e = sero, xx
elif d == 2:
    s, e = 0, xx
elif d == 3:
    s, e = sero-xx, 0
elif d == 4:
    s, e = sero-xx, garo

print(pos)
print(dir)
print(s,e)