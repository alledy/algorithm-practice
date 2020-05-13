class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i+1
                switch = False
                while j < len(nums) and switch is False:
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        switch = True
                    j += 1
                if switch is False:
                    break
            i += 1
