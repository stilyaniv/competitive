def find_nums_pair_brute(nums: list[int]) -> int:
    for i in nums:
        for j in nums:
            if i != j and i+j == 2020:
                return i*j
    return 0

def find_nums_pair(nums: list[int]) -> int:
    for i, _ in enumerate(nums):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]

    return 0

def find_nums_triple(nums: list[int]) -> int:
    for i, _ in enumerate(nums):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i] * nums[j] * nums[k]
    return 0


if __name__ == '__main__':
    nums = [int(line.strip()) for line in open("day_1_input.txt")]
    print(nums)
    print(find_nums_pair(nums))
