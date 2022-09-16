t = (1, '2', 3, '4', 5)
tmp = (str(i) for i in t)
ans = int(''.join(tmp))
print(f'変換後の数値 : {ans}')