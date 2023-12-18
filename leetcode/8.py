#!usr/bin/python
# -*- coding:UTF-8 -*-

# 08.leetcode题目讲解（Python）：字符串转整数

# class Solution:
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         raw_str = str
#         # set of valid
#         valid_set = {
#             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', ' '
#         }
#         # set of num
#         num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
#         # set of sign
#         sign_set = {'+', '-'}
#         # set of space

#         k = 0  # current location
#         m = 0  # the number of signs
#         p = 0  # the last space location
#         n = 0  # the last signs location
#         i = 0  # the number of 'num'

#         temp_str = ''

#         # case1: str is Null
#         if len(raw_str) == 0:
#             return 0

#         # case2: illegal words at begining
#         if raw_str[0] not in valid_set:
#             return 0

#         for s in raw_str:
#             if s in sign_set:
#                 # the sign after num is not valid
#                 if i > 0:
#                     break

#                 m = m + 1
#                 n = k
#                 # case3: if there are more than 1 signs
#                 if m > 1:
#                     return 0
#             if s == ' ':
#                 #  the space after num is not valid
#                 if i > 0:
#                     break
#                 p = k

#             if s in num_set:
#                 # case4: if the last sign location before last space location
#                 if p > n and m > 0:
#                     return 0
#                 i = i + 1
#                 temp_str = temp_str + s

#             if s not in valid_set:
#                 k = k + 1
#                 break

#             k = k + 1

#         # case5: have no number in str:
#         if i == 0:
#             return 0
#         else:
#             # the num with sign
#             if m > 0:
#                 temp_str = raw_str[n] + temp_str

#         covert_int = int(temp_str)

#         # overflow
#         if covert_int >= 2**31 - 1:
#             return 2**31 - 1
#         if covert_int <= (-2**31):
#             return (-2**31)

#         return covert_int


# test


# class Solution:
#     def myAtoi(self, s):
#         i = 0
#         n = len(s)

#         while i < n and s[i] == ' ':  # skipping space characters at the beginning
#             i += 1

#         positive = 0
#         negative = 0

#         if i<n and s[i] == '+':
#             positive += 1  # number of positive signs at the start in string
#             i += 1

#         if i<n and s[i] == '-':
#             negative += 1  # number of negative signs at the start in string
#             i += 1

#         ans = 0.0

#         while i < n and '0' <= s[i] <= '9':
#             ans = ans * 10 + (ord(s[i]) - ord('0'))  # converting character to integer
#             i += 1

#         if negative > 0:  # if negative sign exists
#             ans = -ans

#         if positive > 0 and negative > 0:  # if both +ve and -ve signs exist, Example: +-12
#             return 0

#         INT_MAX = 2**31 - 1
#         INT_MIN = -2**31

#         if ans > INT_MAX:  # if ans > 2^31 - 1
#             ans = INT_MAX

#         if ans < INT_MIN:  # if ans < -2^31
#             ans = INT_MIN
#         print(i)
#         return int(ans)










# class Solution:
#     def myAtoi(self, s):
#         l = len(s)
#         i = 0
#         p,neg =0,0
#         n =int(1)
#         num = ["0","1","2","3","4","5","6","7","8","9","."]
#         if l < 2 and  s not in num:
#             return 0


#         while i < l  and s[i] ==" ":
#             i +=1
            
#         if i<l and s[i] =="+":
#             p +=1
#             i +=1

#         if i <l and s[i] =="-":
#             neg +=1
#             n = int(-1)
#             i +=1
            
#         I = i

#         if neg >0 and p >0:
            
#             return 0
#         if i < l and s[i]=="." :
#             return 0
#         ans =0
#         h = 10
#         while i < l and s[i]=="0":
#             i +=1

#         while i <l  and s[i] !=" " :
            
#             if s[i] not in num  :
#                 break
            
#             if s[i]==".":
                
#                 print(s[i-1])
#                 ans = int(s[i-1])*n
#                 break
#             print(h)
#             ans = (int(ans*h)+int(s[i]))
            
#             i +=1
#         # print(ans)
#         ans = ans*n

#         max = 2**31-1
#         min = -2**31

#         if ans > max:
#             ans = max
#         if ans < min:
#             ans = min

#         # print(ans)
#         return ans



##########################


class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value
    


s = Solution()
print(s.myAtoi("-42"))

