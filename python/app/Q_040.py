l = [1, '22', 3, '444', 0.0, '5']
l2 = [i for i in l if isinstance(i, int)]
print(f'最大値 : {max(l2)}')
print(f'最小値 : {min(l2)}')
