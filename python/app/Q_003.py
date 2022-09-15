def squaring(num) -> int:
    ans = num ** 2
    return ans

if __name__ == '__main__':
    input_var = int(input('好きな整数を入力してください > '))
    ans = squaring(input_var)
    print(f'{input_var}の二乗値 : {ans}')