# import ast
# s = '{"A": 111, "B": 222, "C": 333}'
# ans = ast.literal_eval(s)
# print(f'変換した辞書 : {ans}')
# print(type(ans))

import json
s = '{"A": 111, "B": 222, "C": 333}'
ans = json.loads(s)
print(f'変換した辞書 : {ans}')
print(type(ans))

ans2 = json.dumps(ans)
print(f'戻し : {ans2}')
print(type(ans2))
