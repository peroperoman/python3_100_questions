words = ['Python', 'Ruby', 'PHP', 'JavaScript']
ans = words[0]
for word in words[1:]:
    if len(word) < len(ans):
        ans = word
print(f'一番短い単語 : {ans}')