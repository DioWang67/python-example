#!usr/bin/python
# -*- coding:UTF-8 -*-


# 06.leetcode题目讲解（Python）：Z字形变换


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # no need to convert
        if numRows == 1:
            return(s)

        zlist = []
        sc = ""
        n = numRows

        # create null list
        while n:
            zlist.append([])
            n = n - 1
            # print(zlist)

        j = 0
        for a in s:
            if j == 0:
                # direction change
                coverse = False
            zlist[j].append(a)
            if j + 1 < numRows:
                if coverse:
                    j = j - 1
                else:
                    j = j + 1
            else:
                j = j - 1
                # direction change
                coverse = True
            print(zlist)
        # get the converted string
        for z in zlist:
            # print(z)
            for t in z:
                # print(sc)
                sc = sc + t
        return(sc)

if __name__ =="__main__" :
    a = Solution()
    s="SDTFYHJK"
    numRows=2
    print(a.convert(s,numRows))