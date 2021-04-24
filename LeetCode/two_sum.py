class Solution:
    def twoSum(self, nums, target):
        dictionary = dict()
        pos = 0
        while pos < len(nums):
            if (target - nums[pos]) not in dictionary:
                dictionary[nums[pos]] = pos
                pos += 1
            else:
                return [dictionary[target - nums[pos]], pos]