t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
ans = [i for i in t if isinstance(i, tuple)]
print(f'タプル内に含まれるタプルの数 : {len(ans)}')
