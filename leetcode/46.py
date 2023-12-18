# def permute(nums):
#     def backtrack(start):
#         # 如果達到了數組的末尾，表示已經找到一個排列，將其添加到結果列表中
#         print(nums[:])
#         if start == len(nums):
#             result.append(nums[:])
#             return
#         # 對於每個還未使用過的元素，進行遞迴探索
#         # print(start, len(nums))
#         for i in range(start, len(nums)):
#             # 交換當前元素和第一個元素
#             nums[start], nums[i] = nums[i], nums[start]
#             # 遞迴進入下一層
#             backtrack(start + 1)
#             # 恢復原始狀態，這是回溯的過程
#             nums[start], nums[i] = nums[i], nums[start]

#     # 存放結果的列表
#     result = []
#     # 開始遞迴
#     backtrack(0)
#     return result

# # 測試
# nums = [1, 2, 3]
# result = permute(nums)
# print(result)



def permute(nums):
    result = [[]]
    
    for num in nums:
        new_permutations = []
        for perm in result:
            for i in range(len(perm)+1):
                new_permutations.append(perm[:i] + [num] + perm[i:])
        result = new_permutations
    
    return result

# 測試
nums = [1, 2, 3]
result = permute(nums)
print(result)