strings = input('文字列を入力してください > ')
vowels = ["a", "i", "u", "e", "o"]
ans = ""
for string in strings:
    if not string in vowels:
        ans += string
print(f'作成した文字列 : {ans}')