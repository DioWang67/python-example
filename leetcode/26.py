



class Solution:
    def removeDuplicates(self, nums) -> int:
        slow,fast = 0,1
        nums_len=len(nums)
        if nums_len <= 1:
            return nums_len
        while fast < nums_len:
            if nums[slow] != nums[fast]:
                slow +=1
                nums[slow]=nums[fast]
            fast +=1
        
        return slow+1

nums=[1,2,2,3,3,3,4,4,4,4,4]

if __name__== '__main__':
	s = Solution()
	print(s.removeDuplicates(nums))