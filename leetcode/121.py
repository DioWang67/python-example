


class Solution:
    def maxProfit(self, prices):


    	len_prices = len(prices)
    	# print(len_prices)
    	one = ""
    	two = ""
    	three= ""
    	result = 0
    	t_prices = []
    	for i in range(len_prices):

    		one = prices[i]
    		t_prices = prices[i:]
    		# print(t_prices)

    		for s in range(len(t_prices)):

    			two = t_prices[s]
    			# print(two)
    			three = 0-(one - two )
    			# print(three)
    			if three > result :
    				result = three
    				# print(result)
    		# print("###########################################")
    	return result



class Solution1:
    def maxProfit(self, prices):
        minprice = 10010
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxprofit:
                maxprofit = price - minprice
        return maxprofit









if __name__== '__main__':

    prices = [1,3,4,99999,5,1,5,6,7,8,4,3,2,4,5,3,2,4,5,3,2,4,3,2,3,2,34,3,4,3,4,3,4,3,666,4,12,312,31,23,13,12,31,23,123,12,312,3,123,14,4,12,231,2,14,12,123,12,312,7,7,77777]



    s = Solution()
    print(s.maxProfit(prices))
