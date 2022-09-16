l = [1, 2, 3, 4, 5]
for i, v in enumerate(l):
    if i % 2 == 0:
        l.insert(i, 'list')
print(f'"list"を追加したリスト : {l}')