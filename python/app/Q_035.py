l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
ans = [i for i in l if isinstance(i, int)]
print(f'整数型に絞り込んだリスト : {ans}')