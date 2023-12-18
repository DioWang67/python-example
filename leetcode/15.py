#!usr/bin/python
# -*- coding:UTF-8 -*-



# 15.leetcode题目讲解（Python）：三数之和


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print(type(len(nums)))
        len_nums = len(nums)
        nums.sort()
        r = []
        for i,a in enumerate(nums):
            print(i,a)
            # j=i+1
            # while j< len_nums :

            #     res1 = (nums[i]+nums[j])*-1

            #     if res1 in nums[i:]  :

            #         print(nums[i],nums[j])
            #         # print(res1)
            #         r.append([nums[i],nums[j],res1])
            #         # return(r)
            #     j=j+1
        # return(r)
                    
    


# s = Solution()
# nums = [-3,1,2]
# print(s.threeSum(nums))



        # nums.sort()
        # L, res = len(nums), []
        # for i in range(L-2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     target = -1 * nums[i]
        #     j,k = i + 1, L - 1
        #     while j<k:
        #         if nums[j]+nums[k] == target:
        #             res.append([nums[i], nums[j], nums[k]])
        #             j = j + 1
        #             while j<k and nums[j] == nums[j-1]:
        #                 j = j + 1
        #         elif nums[j] + nums[k] < target:
        #             j = j + 1
        #         else:
        #             k = k - 1
        # return res

#solution

class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = set()
    
        for i in range(len(nums) - 2):
            firstNum = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                secondNum  = nums[j]
                thirdNum = nums[k]

                potentialSum = firstNum + secondNum + thirdNum 
                if potentialSum > 0:
                    k -= 1
                elif potentialSum < 0:
                    j += 1
                else:
                    triplets.add((firstNum , secondNum ,thirdNum))
                    j += 1
                    k -= 1
        return triplets
    


s = Solution()
nums = [-3,4,1,2,-4,0]
print(s.threeSum(nums))