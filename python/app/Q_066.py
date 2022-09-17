d1 = {'A': 111, 'B': 222, 'C': 333}
d2 = {'D': 444, 'E': 555}
d3 = {'F': 666}
ans = {}
for i in [d1, d2, d3]:
    ans.update(i)
print(f'連結した辞書 : {ans}')