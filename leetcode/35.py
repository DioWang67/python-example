# class Solution:
#     def searchInsert(self, nums, target):
        
#         le = len(nums)
#         if le == 0:
#             return 0

#         if target > nums[-1]:
#             return le
#         elif target < nums[0]:
#             return 0
#         elif target == nums[-1]:
#             return le - 1
#         elif target == nums[0]:
#             return 0

#         lo = 0
#         hi = le - 1

#         while lo < hi:
#             if (hi - lo) // 2 > 0:
#                 mid = lo + (hi - lo) // 2
#                 if nums[mid] < target:
#                     lo = mid
#                 elif nums[mid] > target:
#                     hi = mid
#                 elif nums[mid] == target:
#                     return mid
#             else:
#                 return hi

#         return hi


class Solution:
    def searchInsert(self, nums, target):
        count = len(nums)

        if count == 0 :
            return 0
        
        for i in range(count):
            if nums[i]== target :
                return i 
            elif target > nums[i-1] and target < nums[i] :
                return i 
            elif target < nums[i]:
                return i
        if target == 0:
            return 0
        return count    
 


if __name__== '__main__':
    s = Solution()

    nums = [2,3,6]
    target = 5
    print(s.searchInsert(nums,target))