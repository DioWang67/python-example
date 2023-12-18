#!usr/bin/python
# -*- coding:UTF-8 -*-

# 17.leetcode题目讲解（Python）：电话号码的字母组合


class Solution:
    def letterCombinations(self, digits):

        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        type_dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = [""]

        for d in digits:
            temp = []
            if d in type_dic.keys():  #獲取字典中所有的鍵（keys）
                print(d)
                for c in type_dic[d]:
                    print(c)
                    for r in res:
                        print(r)
                        temp.append(r + c)
                res = temp

        return res




s = Solution()
digits = "29"
print(s.letterCombinations(digits))