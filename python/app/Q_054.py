l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = [tuple(l[i:i+3]) for i in range(0, len(l), 3)]
for i, v in enumerate(ans, start=1):
    print(f'{i}行目の値 : ', *v)