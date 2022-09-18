s = 'This is the Python exercise.'
strings = list(s.split(' '))
tmp = [string for string in strings if 't' not in string]
ans = ' '.join(tmp)
print(f'削除後の文字列 : {ans}')
