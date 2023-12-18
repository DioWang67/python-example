





class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        ans = 0
        for i in range(len(nums)):
            # print(i)
            ans ^= nums[i]
        print("#####")
        return ans





















if __name__== '__main__':

    nums = [1,1,2]



    s = Solution()
    print(s.singleNumber(nums))
