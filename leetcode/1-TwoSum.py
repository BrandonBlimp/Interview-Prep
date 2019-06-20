# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i_1 in range(0, len(nums)):
            num_1 = nums[i_1]
            for i_2 in range(i_1+1, len(nums)):
                num_2 = nums[i_2]
                if num_1 + num_2 == target:
                    return [i_1, i_2]
            