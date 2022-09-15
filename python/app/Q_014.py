def cal(input_var) -> int:
    tmp = str(input_var)*3
    ans = input_var + int(tmp)
    return ans

if __name__ == '__main__':
    input_var = int(input('整数を入力してください > '))
    res = cal(input_var)
    print(res)