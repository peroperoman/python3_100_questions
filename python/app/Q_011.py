def cal_bmi(num1, num2) -> int:
    ans = num1 / (num2 / 100)**2
    return ans

if __name__ == '__main__':
    res = cal_bmi(58, 170)
    print(f'BMI = {res}')