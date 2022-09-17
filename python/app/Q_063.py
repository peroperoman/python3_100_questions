l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5]
ans1 = set(l1).issubset(set(l2))
ans2 = set(l2).issubset(set(l1))
print(f'l1はl2に含まれている : {ans1}')
print(f'l2はl1に含まれている : {ans2}')