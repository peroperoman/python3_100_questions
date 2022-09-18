l = ['アメリカ', 'カナダ', 'スイス', 'メキシコ', 'セントルシア', 'タイ']
chk_words = ['サ', 'シ', 'ス', 'セ', 'ソ']
print('サ行を含む単語:')
for word in l:
    for chk_word in chk_words:
        if chk_word in word:
            print(word)
            break