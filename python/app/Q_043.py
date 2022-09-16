l = [4, 'aaa', 2, 'ddd', 'ccc', 3, 1, 'bbb']
l2 = sorted([i for i in l if isinstance(i, int)])
l3 = sorted([i for i in l if isinstance(i, str)])
ans = l2 + l3
print(f'ソートしたリスト : {ans}')