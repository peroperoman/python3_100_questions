l = [1, 2, None, 3]
for i in l:
    if i is None:
        i = 10000
    print(i)