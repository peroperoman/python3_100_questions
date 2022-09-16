from audioop import avg


l1 = [4, 6, 9, 2]
l2 = [3, 5, 7]
l3 = [1, 9, 7]
tmp = [l1, l2, l3]
ans = sorted(tmp, key=lambda i: sum(i) / len(i), reverse=True)
print(f'平均値が最も高いリスト : {ans[0]}')
