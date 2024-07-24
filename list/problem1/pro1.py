nums=[2,7,11,15]
n=len(nums)
class Solution:
    def twoSum(self, nums, target):
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    #nums.append(nums[i],nums[j])
                    return [i,j]
        return []
target=9
A=Solution()
print(A.twoSum(nums,target))
