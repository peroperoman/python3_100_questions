def cal_bmi(height, weight) -> float:
    ans = weight / (height / 100)**2
    return ans

if __name__ == '__main__':
    height = float(input('身長を入力してください(cm) > '))
    weight = float(input('体重を入力してください(kg) > '))
    res = cal_bmi(height, weight)
    print(f'BMI = {res}')