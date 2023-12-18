#!usr/bin/python
# -*- coding:UTF-8 -*-

# 05.leetcode题目讲解（Python）：最长回文子串




# class Solution:
#     def longestPalindrome(self, s):

#         mlen = len(s)
#         while True:
#             i = 0
#             while i + mlen <= len(s):
#                 sl = s[i:i + mlen]
#                 # print(i + mlen,mlen)
#                 print(sl)
#                 sr = sl[::-1]
#                 # print(sr)

#                 if sl == sr:
#                     return sl
#                 i = i + 1
#             mlen = mlen - 1
#         print("#####")


############################################
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n <= 1:
#             return s

#         dp = [[False for _ in range(n)] for _ in range(n)]
#         print(dp)
#         max_start = 0
#         max_len = 1

#         for j in range(1, n):
#             for i in range(j):
#                 if s[i] == s[j]:
#                     if j - i <= 2:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#                 if dp[i][j] and (j - i + 1) > max_len:
#                     max_len = j - i + 1
#                     max_start = i
#         return s[max_start: max_start + max_len]


# if __name__ =="__main__" :
#     S = Solution()
#     s="abacrge"
#     print(S.longestPalindrome(s))




# def is_palindrome(s):
#     return s == s[::-1]

# def longest_palindromic_substring(s):
#     n = len(s)
#     longest =""
#     for i in range(n):
#         for j in range(n):
#             substr = s[i:j+1]
#             if is_palindrome(substr) and len(substr) > len(longest):
#                 longest =substr
#     return longest

# # 測試程式碼
# if __name__ == "__main__":
#     s = "babad"
#     result = longest_palindromic_substring(s)
#     print("最長回文子串：", result)


####################################################3
# #中心擴展法
# def longest_palindromic_substring(s):
#     n = len(s)
#     longest = ""

#     def expand_around_center(left, right):
#         while left >= 0 and right < n and s[left] == s[right]:
#             left -= 1
#             right += 1
#             # print(s[left])
#             print(left,right,i)
#         return s[left+1:right]

#     for i in range(n):
#         odd_palindrome = expand_around_center(i, i)
#         # print(odd_palindrome)
#         even_palindrome = expand_around_center(i, i+1)
#         # print(even_palindrome)
#         longest = max(longest, odd_palindrome, even_palindrome, key=len)
        

#     return longest

# # 測試程式碼
# if __name__ == "__main__":
#     s = "5123216"
#     result = longest_palindromic_substring(s)
#     print("最長回文子串：", result)

#################################################
#動態規劃法
# def longest_palindromic_substring(s):
#     n = len(s)
#     dp = [[False] * n for _ in range(n)]
#     longest = ""

#     for i in range(n):
#         dp[i][i] = True
#         longest = s[i]

#     for j in range(1, n):
#         for i in range(j-1, -1, -1):
#             if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
#                 dp[i][j] = True
#                 if j - i + 1 > len(longest):
#                     longest = s[i:j+1]

#     return longest

# # 測試程式碼
# if __name__ == "__main__":
#     s = "babad"
#     result = longest_palindromic_substring(s)
#     print("最長回文子串：", result)











# def longest_palindromic_substring(s):
#     l = len(s)
#     if l ==1 :
#         return s
#     if l =="":
#         return 0
#     start = 1
#     secend = 0
#     secend2 =0
#     # Reversed =s[::-1]
  
#     res = s[0]

#     while start < l:
#         secend = 0
#         secend2 =0
#         w=start-1
#         end = start+2 
#         one = s[w:end]
#         two = one[::-1]
#         three = s[w:end-1]
#         four = three[::-1]

#         if three == four and len(three) >= len(res):
#             res = three

#         start +=1

#         five = ""
#         six =""
        
#         while  secend<l :
#             # print(secend)
#             secend +=1
#             secend2 -=1
#             five = s[w:secend]
#             six = five[::-1] 
#             seven = s[w+secend2:end+secend]
            
#             eight =seven[::-1]
#             print(seven,eight)
#             if five == six and len(five) > len(res):
#                 res =five
#             if seven == eight and len(seven) > len(res):
#                 # print(seven,eight)
#                 res =seven
#             # print(five)
#     return res

# # 測試程式碼
# if __name__ == "__main__":
#     s = "12233221"
#     result = longest_palindromic_substring(s)
#     print("最長回文子串：", result)



class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            
            print(s[left],s[right])
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            print(s[left + 1:right])   
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str
    

if __name__ == "__main__":
    l = Solution()
    s = "aabbaa"
    result = l.longestPalindrome(s)
    print("最長回文子串：", result)
