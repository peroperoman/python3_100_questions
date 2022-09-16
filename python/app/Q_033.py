l1 = ['Python', 'Ruby', 'PHP', 'JavaScript']
l2 = ['Java', 'Ruby', 'Golang', 'Python', 'TypeScript', 'Python']
ans = [i for i in l1 if i in l2]
print(f'共通する値を格納したリスト : {ans}')