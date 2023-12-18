import sys

def threeSumClosest(nums, target):
    nums.sort()  # 將整數列表進行排序
    closest_sum = sys.maxsize  # 初始化最接近目標數字的和為一個較大的數值
    min_diff = sys.maxsize  # 初始化最小差值為一個較大的數值

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            diff = abs(total - target)

            if diff < min_diff:
                min_diff = diff
                closest_sum = total

            if total == target:
                return total
            elif total < target:
                left += 1
            else:
                right -= 1

    return closest_sum


nums = [-1, 2, 1, -4]
target = -1

print(threeSumClosest(nums,target))