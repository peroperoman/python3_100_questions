d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
ans = min(d.keys(), key=lambda k: d[k])
print(f'最小のValueを持つKey : {ans}')