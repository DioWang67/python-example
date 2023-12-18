










# class Solution:
#   def majorityElement(self, nums):
#     ans = None
#     count = 0

#     for num in nums:
#       if count == 0:
#         ans = num
#         print (ans)
#       count += (1 if num == ans else -1)
#       # print(count)

#     return ans

class Solution:
  def majorityElement(self, nums):
    ans = None
    count = 0

    for num in nums:
      # print(ans,num)
      if count == 0:
        ans = num
        # print(ans)
      
      if num == ans :
      	count -=1 
      else:
      	count +=1 
      	
      print(count)
    print("####################")

    return ans







if __name__== '__main__':

    nums = [3,2,3]




    s = Solution()
    print(s.majorityElement(nums))
