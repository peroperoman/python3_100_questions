l = [{'id': 10000, 'feature': {'name': 'Michael', 'height': 180.3, 'weight': 63.7, 'skills': {'IT': ['Python', 'Golang', 'SQL'], 'Others': ['Chinese', 'Math']}}}, 
{'id': 10001, 'feature': {'name': 'Nancy', 'height': 156.7, 'weight': 39.7, 'skills': {'IT': ['Java', 'SQL', 'JavaScript'], 'Others': ['Accounting']}}}]

tmp = [i['feature']['skills']['IT'] for i in l]
a, b = tmp
ans = set(a) & set(b)
print(ans)