#!usr/bin/python3
# -*- coding:UTF-8 -*-

# class Solution():
# 	def plusOne(self,digits):
# 		digits = [1,2,9]
# 		for i in range(len(digits)-1,-1,-1):
# 			if digits[i] != 9:
# 				digits[i] += 1
# 				break

# 			digits[i] = 0
# 		if digits[0] == 0:
# 			digits.insert(0,1)

# 		return digits

class Solution():
	def plusOne(self, digits):
	    digits = [0] + digits

	    print(digits[-1])
	    # print(digits[len(digits) - 1])
	    digits[-1] += 1

	    print(digits)

	    for i in range(len(digits)-1, 0, -1):
	        # print(i)
	        if digits[i] != 10:
	            break
	        else:
	            digits[i] = 0
	            digits[i - 1] += 1
	            print(digits[i - 1])
	        
	    if digits[0] == 0:
	        return digits[1:] 
	    else:
	        return digits



if __name__== '__main__':
	s=Solution()
	digits = [1,5,9,9]
	print(s.plusOne(digits))