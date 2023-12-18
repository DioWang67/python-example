# class Solution:
#     def removeElement(self, nums, val) -> int:
#         i = 0
#         while i < len(nums) :
#             if nums[i] == val :
#                 nums.remove(nums[i])
#             else :
#                 i = i+1
#         return len(nums)
    
# s = Solution()
nums = [3,2,2,3]
val=3
# print(s.removeElement(nums,val))
nums2=[]

a = len(nums)
for i in range(a):
    if nums[i] == val :
        continue
    else:
        nums2.append(nums[i])
print(nums2)
print(len(nums2))