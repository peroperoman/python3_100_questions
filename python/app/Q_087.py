l = [1, 2, None, False, '3', '4', None, True]
ans = [i for i in l if i is True or i is None]
print(f'TrueとNoneの数 : {len(ans)}')