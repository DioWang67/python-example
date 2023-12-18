#!usr/bin/python
# -*- coding:UTF-8 -*-

# 10.leetcode题目讲解（Python）：正则表达式匹配



# class Solution:
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         in_str = s
#         pt = p

#         if not pt:
#             return not in_str

#         first_match = bool(in_str) and pt[0] in {in_str[0], '.'}

#         if len(pt) >= 2 and pt[1] == '*':
#             return (self.isMatch(in_str, pt[2:])
#                     or first_match and self.isMatch(in_str[1:], pt))
#         else:
#             return first_match and self.isMatch(in_str[1:], pt[1:])


# s = Solution()
# print(s.isMatch("ab", "a*ab"))





# def isMatch(s: str, p: str) -> bool:
#     m, n = len(s), len(p)
#     dp = [[False] * (n + 1) for _ in range(m + 1)]
#     print(dp)
#     dp[0][0] = True

#     for j in range(1, n + 1):
#         if p[j - 1] == '*':
#             dp[0][j] = dp[0][j - 2]

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if p[j - 1] == s[i - 1] or p[j - 1] == '.':
#                 dp[i][j] = dp[i - 1][j - 1]
#             elif p[j - 1] == '*':
#                 dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))

#     return dp[m][n]

# # 例子
# s = "aaa"
# p = "aa*"
# result = isMatch(s, p)
# print(result)




class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        print("a")
        key = (i, j)
        if key in cache:
            return cache[key]

        if i == -1 and j == -1:
            cache[key] = True
            return True

        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            
            if k == -1:
                cache[key] = True
                return cache[key]
            
            cache[key] = False
            return cache[key]
        
        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]

        if p[j] == '*':
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return cache[key]
            
            if p[j - 1] == s[i] or p[j - 1] == '.':
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]
        
        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]
    
s = Solution()
print(s.isMatch("ab", "a*ab"))
