class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        l = len(nums)

        for i in range(l):
            if target - nums[i] in h:
                return [h[target - nums[i]],i]
            else:
                h[nums[i]] = i
        