class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        
        n = len(nums)
        
        if n % 2 == 1:
            return nums[n // 2]
        else:
            mid1, mid2 = n // 2 - 1, n // 2
            return (nums[mid1] + nums[mid2]) / 2.0

# Usage
nums1 = [1, 3]
nums2 = [3, 4]
solution = Solution()
median = solution.findMedianSortedArrays(nums1, nums2)
print("Median:", median)
