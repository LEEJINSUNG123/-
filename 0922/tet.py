a = [1, 2, 3, 4]

N = len(a)
cnt = 0
cnt2 = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                for m in range(N):
                    for n in range(N):
                        print(a[i], a[j], a[k], a[l], a[m], a[n], )
