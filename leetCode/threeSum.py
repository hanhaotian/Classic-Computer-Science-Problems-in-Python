def three_sum2(nums: List[int]) -> List[List[int]]:
    res = set()
    length = len(nums)
    nums = sorted(nums)
    if nums[0] <= 0 and nums[length - 1] >= 0:
        for i in range(length-2):
            if nums[i] > 0:
                break
            first = i + 1
            last = length - 1
            while first < last:
                if (first >= last) or (nums[i] * nums[last] > 0):
                    break
                result = nums[i] + nums[first] + nums[last]
                if result == 0:
                    res.add((nums[i], nums[first], nums[last]))
                if result <= 0:
                    temp = nums[first]
                    while first < last and temp == nums[first]:
                        first += 1
                else:
                    temp = nums[last]
                    while first < last and temp == nums[last]:
                        last -= 1

            temp = nums[i]
            while nums[i] == temp and i < nums.__len__() - 1:
                i += 1
    return [list(v) for v in res]
