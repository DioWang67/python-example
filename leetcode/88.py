


class Solution:
    def merge(self, nums1,m, nums2, n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        index = m + n - 1
        # print(index)
        while index1 >= 0 and index2 >= 0:

            if nums1[index1] < nums2[index2]:
                # print(index1,index2)
                nums1[index] = nums2[index2]
                # print(nums1[index],nums2[index2])
                index2 -= 1
            else:
                nums1[index] = nums1[index1]
                # print(nums1)
                index1 -= 1
            index -= 1

        nums1[:index2+1] = nums2[:index2+1]
        print(nums1[:index2+1],nums2[:index2+1])
        
        return nums1

if __name__== '__main__':

    nums1 = [1,2,3,4,0,0,0]
    m = 4
    nums2 = [2,5,6]
    n = 2



    s = Solution()
    print(s.merge(nums1,m,nums2,n))