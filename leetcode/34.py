

class Solution:
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]

# 測試
s = Solution()
nums = [5, 7, 7,7, 8, 8, 10]
target = 7
print(s.searchRange(nums, target))  # 預期輸出：[3, 4]


# left = 0
# right = 5
# mid = left + (right - left) // 2
# print(mid)