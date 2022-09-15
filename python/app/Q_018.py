strings = input('文字列を入力してください > ')
ans_d = {string: strings.count(string) for string in strings}
print(ans_d)
