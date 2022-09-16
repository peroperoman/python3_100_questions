a_word = input('1つ目の英単語を入力してください > ')
b_word = input('2つ目の英単語を入力してください > ')
c_word = input('3つ目の英単語を入力してください > ')

ans = [a_word, b_word, c_word]
ans.sort()

print(', '.join(ans))