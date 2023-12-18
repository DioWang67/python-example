#!usr/bin/python
# -*- coding:UTF-8 -*-

import time


class Solution:
    # @return a tuple, (index1, index2)
    # 8:42

    # def twoSum(self, num, target):
    #     map = {}
    #     for i in range(len(num)):
    #         if num[i] not in map:
    #             map[target - num[i]] = i 
    #             print(map)
    #             print(i)
    #         else:
    #             return map[num[i]], i

    #     return -1,-1

    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        return []

			
nums=[5,4]
target = 9
if __name__== '__main__':
	s = Solution()
	print(s.twoSum(nums,target))

















# class solution():

# 	def  twosum(self,nums,target):
# 		i = 0 
# 		while i < len(nums):
# 			if i == len(nums) -1 :
# 				return "no solution here"
# 			r = target - nums[i]

# 			num_follow = nums[i+1:]
# 			print(num_follow)
# 			if r in num_follow:
# 				return[i,num_follow.index(r)+i+1]
# 			i = i+1
			
# nums=[0,2,10,8]
# target = 12		
# if __name__== '__main__':
# 	s = solution()
# 	print(s.twosum(nums,target))