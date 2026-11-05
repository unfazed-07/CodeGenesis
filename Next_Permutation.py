class Solution:
    def nextpermutation(self, nums):
        n = len(nums)
        idx = -1

        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                idx = -1
                break;
        
        if idx == -1:
            nums.reverse()
            return nums


        for i in range(n-1, idx, -1):
            if nums[i]>nums[idx]:
                nums[i] ,nums[idx] = nums[idx], nums[i]
                break;

        left = idx+1
        right = n-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        return nums

nums = list(map(int, input().split()))
result = Solution().nextpermutation(nums)
print(result)