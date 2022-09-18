methods = dir(list)
ans = [method for method in methods if not method.startswith('__')]
print(f'リストで使えるメゾット一覧:\n {ans}')