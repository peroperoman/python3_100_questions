telephone_numbers = ['080-1111-1111', '090-1111-1111', '090-2222-2222', '080-2222-2222']
ans = [telephone_number for telephone_number in telephone_numbers if telephone_number.startswith('080')]
print(f'080で始まる電話番号 : {ans}')
