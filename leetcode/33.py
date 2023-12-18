

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            print("a",left,mid) 
            if nums[mid] == target:
                # print(nums[mid])
                return mid
            
            if nums[left] <= nums[mid]:
                print(nums[left],nums[mid])
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1


######


# class Solution:
#     def search(self, nums, target):
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 return i
#         return -1


# 測試
s = Solution()
nums = [4, 5, 6, 7,8,9, 0, 1, 2]
target = 2
print(s.search(nums, target))  # 預期輸出：4