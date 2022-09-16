def cal_total(nums:list) -> int:
    ans = 0
    for num in nums:
        ans += num
    return ans

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    res = cal_total(nums)
    print(f'リスト内の合計 : {res}')