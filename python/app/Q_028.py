def search_max(nums:list) -> int:
    ans = 0
    for num in nums:
        if ans <= num:
            ans = num
    return ans

if __name__ == '__main__':
    nums = [1, 5, 3, 2, 4]
    res = search_max(nums)
    print(f'リスト内の最大値 : {res}')