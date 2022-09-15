def cal(a, b) -> int:
    ans = a - b
    if ans < 0:
        ans = -ans
    return ans

if __name__ == '__main__':
    a = int(input('1つ目の整数を入力してください > '))
    b = int(input('2つ目の整数を入力してください > '))
    res = cal(a, b)
    print(f'計算結果 : {res}')