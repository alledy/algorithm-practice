class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_arr = [0] * len(nums)
        sum_arr[0] = nums[0]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if sum_arr[i-1] > 0:
                sum_arr[i] = sum_arr[i-1] + nums[i]
            else:
                sum_arr[i] = nums[i]
        return max(sum_arr)
