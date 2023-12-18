#!usr/bin/python
# -*- coding:UTF-8 -*-

# 题目：

# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

# 请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 


# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
# 中位数是 2.0
# 示例 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 中位数是 (2 + 3)/2 = 2.5






class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums = nums1 + nums2
        self.nums.sort()
        print(self.nums)
        size = len(self.nums)
        print(size,size % 2)
        if size % 2 == 1:
            return self.nums[size//2]

        if size % 2 == 0:
            return (self.nums[size//2] + self.nums[size//2 - 1])/2


if __name__ == "__main__" :
    s = Solution()
    nums1 = [8, 7,10]
    nums2 = [3, 4,7]
    print(s.findMedianSortedArrays(nums1,nums2))

##############################################

# def findMedianSortedArrays(nums1, nums2):
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1

#     x, y = len(nums1), len(nums2)
#     low, high = 0, x

#     while low <= high:
#         partitionX = (low + high) // 2
#         partitionY = (x + y + 1) // 2 - partitionX

#         maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
#         minX = float('inf') if partitionX == x else nums1[partitionX]

#         maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
#         minY = float('inf') if partitionY == y else nums2[partitionY]

#         if maxX <= minY and maxY <= minX:
#             if (x + y) % 2 == 0:
#                 return (max(maxX, maxY) + min(minX, minY)) / 2
#             else:
#                 return max(maxX, maxY)
#         elif maxX > minY:
#             high = partitionX - 1
#         else:
#             low = partitionX + 1

# # 測試
# nums1 = [1, 3]
# nums2 = [2,4,5]
# result = findMedianSortedArrays(nums1, nums2)
# print(result)  # Output: 2.0
