phone_numbers = ['080-1203-4455', '090-9372-9682', '03-9471-5929', '070-3917-5918', '04-8572-8910']
# ans = [phone_number for phone_number in phone_numbers if phone_number.startswith('090') or phone_number.startswith('080') or phone_number.startswith('070')]
ans = [phone_number for phone_number in phone_numbers if phone_number.find('-') == 3]
print(f'携帯電話の番号 : {ans}')
