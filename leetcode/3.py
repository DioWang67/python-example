#!/usr/bin/python3

# 无重复字符的最长子串
# 给定一个字符串，找出不含有重复字符的最长子串的长度。
# 示例：
# 给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
# 给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
# 给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列 而不是子串。

import time

class Solution:
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     len_s = len(s)

    #     I = 1
    #     ans1=""
    #     ans = ""
    #     ans2= ""
    #     r = 0
    #     ans3=""
    #     b = 0
    #     if s == " " :
    #         return 1
    #     if s =="":
    #         return 0

    #     for a in range(len_s):
            
    #         for i in s[b:]  :
    #             ans += i
    #             if i not in ans1 :
    #                 ans1 +=i

    #                 if len(s)==1: 
    #                     ans2 =ans1
    #             else:
    #                r = 1
    #                if len(ans2)<=len(ans1): 
    #                     ans2 =ans1
    #                     ans1 =""
    #                     ans1+=i
    #                if len(ans2) > len(ans1):
    #                     ans1=""
    #                     ans1+=i

    #             # print("1="+ans,"  2="+ans1,"  3="+ans2)
    #             if len(ans1)  > len(ans3) :
    #                 ans3 = ans1
    #             elif len(ans2) > len(ans3):
    #                 ans3 = ans2
    #             # print("ans3="+ans3)
    #         b +=1
    #         ans1=""
    #         ans = ""
    #         ans2= ""
    #     print("ans3="+ans3)  
    #     return len(ans3)

###################################################

    def lengthOfLongestSubstring(self, s):

            dic = {}
            res, last_match = 0, -1
            for i, c in enumerate(s):
                
                if c in dic and last_match < dic[c]:
                    last_match = dic[c]
                    print(dic[c])
                res = max(res, i - last_match)
                # print(res)
                dic[c] = i 
                # print(dic[c])
            return res
    
##############################################
#2023.12.4 自寫 複雜度過高

    # def lengthOfLongestSubstring(self, s: str) -> int:


    #     res = []
    #     res2=[]
    #     l =len(s)
    #     if l ==1:
    #         return l
    #     for a in range(l):
    #         for i in range(a,l):
    #             if i ==l:
    #                 break
    #             if s[i] not in res:
    #                 res.append(s[i])
    #             else:
    #                 if len(res) >len(res2):
    #                     res2 = res
    #                 res=[s[i]]
    #         if len(res) >len(res2):
    #             res2 = res 
    #         res=[]
  
    #     print(res2)        
    #     return len(res2)    
#########################################

    # def lengthOfLongestSubstring(self, s: str) -> int:


    #     res = []
    #     res2=[]
    #     l =len(s)
    #     j=0
    #     if l ==1:
    #         return l
    #     for a in range(l):
    #         for i in range(a,l):
    #             w=s[i:i+1]
    #             print(w)
    #             if w not in res:
    #                 res.append(w)
    #             else:
    #                 if j < len(res):
    #                     j =len(res)
    #                 res=[]
    #                 break

    #     return j

if __name__ == '__main__':
    a=Solution()
    s="abcabcbb"
    print(a.lengthOfLongestSubstring(s))
























        # len_s = len(s)
        # if len_s == 0:
        #     return 0
        # set_s = set(s)
        # print(set_s)
        # # get the max_size of sild window
        # max_len = len(set_s)
        # print(max_len)
        # max_sub_str = ""
        # while max_len:
        #     print(max_len)
        #     if max_len == 1:
        #         return 1
        #     i = 0
        #     while i + max_len <= len_s:
        #         sub_s = s[i:i + max_len]
        #         set_sub = set(sub_s)
        #         # if there is no repeat in sub string
        #         if len(set_sub) == len(sub_s):
        #             max_sub_str = sub_s
        #             return(len(list(max_sub_str)))
        #         i = i + 1
        #     # adjust the size of window
        #     max_len = max_len - 1





    # class Solution:
    # # @return an integer
    # def lengthOfLongestSubstring(self, s):
    #     start = maxLength = 0
    #     usedChar = {}
        
    #     for i in range(len(s)):
    #         if s[i] in usedChar and start <= usedChar[s[i]]:
    #             start = usedChar[s[i]] + 1
    #         else:
    #             maxLength = max(maxLength, i - start + 1)

    #         usedChar[s[i]] = i

    #     return maxLength