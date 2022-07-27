def solution(nums):
    answer = 0
    last = 0

    length = len(nums) // 2
    nums.sort()

    for value in nums:
        if (value != last and answer < length):
            answer += 1
            last = value
    return answer
