t = (1, [2, 3], '4', (5, 6, 7), None, (9, 10))
ans = []
for i in t:
    if isinstance(i, tuple):
        ans.append(i)
    elif isinstance(i, list):
        ans.append(tuple(i))
    else:
        ans.append((i, ))

print(f'変換したタプル : {tuple(ans)}')