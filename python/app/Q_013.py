def conv_per_sec(per_hour_k) -> int:
    per_sec_m = per_hour_k / 3600 * 1000
    return per_sec_m

if __name__ == '__main__':
    per_hour_k = int(input('時速(km/h)を入力してください > '))
    res = conv_per_sec(per_hour_k)
    print(f'秒速 = {res} m/s')