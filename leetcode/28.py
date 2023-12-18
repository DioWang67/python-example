class Solution:
    def strStr(self, haystack, needle):
        # makes sure we don't iterate through a substring that is shorter than needle
        for i in range(len(haystack) - len(needle) + 1):
            # check if any substring of haystack with the same length as needle is equal to needle
            if haystack[i : i+len(needle)] == needle:
                # if yes, we return the first index of that substring
                return i
        # if we exit the loop, return -1        
        return -1
    
if __name__== '__main__':
    s = Solution()
    haystack = "leetcode"
    needle = "leeto"
    print(s.strStr(haystack,needle))