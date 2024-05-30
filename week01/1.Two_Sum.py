import sys
def twoSum(nums, target):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = i
    for num in hash.keys():
        ans = hash.get(target-num)
        if ans != None:
            return [hash[num],ans]