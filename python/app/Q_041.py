l = [0, '1', 3, 2, '4', 5, '7']
l2 = [v for i, v in enumerate(l) if int(v) == i]
print(f'インデックスと値が一致 : {l2}')