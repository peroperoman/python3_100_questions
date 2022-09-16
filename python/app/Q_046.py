l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
ans = [i for i in l if not 'Python' in str(i)]
print(f'文字列"Python"を削除したリスト : {ans}')