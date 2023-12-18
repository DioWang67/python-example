#!usr/bin/python3
# -*- coding:UTF-8 -*-




class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = "hello world qwer eqweqweqweqwd"
        nums = len(s)
        count = 0
        
        s=s.strip()
        print(s)

        l=s.split(' ')
        print(l)
        l=list(l)
        print(l)
        return len(l[-1])


s = Solution()
print(s.lengthOfLastWord(s))