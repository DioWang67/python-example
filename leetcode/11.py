#!usr/bin/python
# -*- coding:UTF-8 -*-

# 11.leetcode题目讲解（Python）：盛最多水的容器


# class Solution:
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         height_list = height
#         # print(height_list)
#         len_height = len(height_list)
#         # print(len_height)
#         if len_height < 2:
#             return 0
#         max_area = 0

#         left = 0
#         right = len_height - 1


#         while left != right:
#             h = min(height_list[left], height_list[right])
#             print(h)
#             w = right - left
#             if max_area < h * w:
#                 max_area = h * w
#             if height_list[left] < height_list[right]:
#                 left = left + 1
#                 print(left)
#             else:
#                 right = right - 1

#         return max_area

class Solution:
    def maxArea(self,height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            print(height[left],height[right])
            w = right - left
            print(w)
            area = h * w
            print(area)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


s=Solution()
height =[1,8,6,2,5,4,8,3,7]
print(s.maxArea(height))


#solution

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left = 0
#         right = len(height) - 1
#         maxArea = 0

#         while left < right:
#             currentArea = min(height[left], height[right]) * (right - left)
#             maxArea = max(maxArea, currentArea)

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1

#         return maxArea