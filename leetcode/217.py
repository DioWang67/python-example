# Time complexity: O(n)
# Space complexity: O(n)
import time 
class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()

        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)
                time.sleep(3)
                print(hset)

        # hset=set((9,9,1,1,2,2,3))
        # print(hset)





if __name__== '__main__':

    nums = [3,2,3]




    s = Solution()
    print(s.containsDuplicate(nums))