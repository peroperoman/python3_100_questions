d = {'B': 222, 'A': 111, 'D': 333, 'C': 444}
ans = dict(sorted(d.items(), key=lambda x: x[1]))
print(f'Valueでソートした辞書 : {ans}')