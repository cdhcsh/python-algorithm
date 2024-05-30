import sys
from itertools import combinations

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return map(lambda t : t[0],set(map(lambda l:(l,None),filter(lambda l : sum(l) == 0,combinations(nums,3)))))

