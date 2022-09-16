word = input('英単語を入力してください > ')
word_len = len(word)
insert_idx = word_len//2
if word_len % 2 == 0:
    word = word[:insert_idx] + '@' + word[insert_idx:]
else:
    word = word[:insert_idx] + '@' + word[insert_idx+1:]

print(f'変換した英単語 : {word}')