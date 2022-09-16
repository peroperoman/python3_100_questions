a_words = input('1つ目の文字列を入力してください > ')
b_words = input('2つ目の文字列を入力してください > ')
ans = ''
for a_word in a_words:
    if a_word in b_words and a_word not in ans:
        ans += a_word
print(f'重複する文字列 : {ans}')