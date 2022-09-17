d = {'B': 222, 'A': 111, 'D': 444, 'C': 333}
ans = {k:v for k, v in d.items() if v % 2 == 0}
print(f'奇数を削除した辞書 : {ans}')