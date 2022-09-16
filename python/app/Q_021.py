words = input('文字列を入力してください > ')
if words[0].isupper():
    print(words*2)
else:
    print(words[0].upper() + words[1:])