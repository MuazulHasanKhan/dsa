class Solution:
    def rob(self, nums: List[int]) -> int:
        
        self.cache  = [-1]*len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            

            # 2 options either too include or exclude the number

            if self.cache[i] != -1:
                return self.cache[i]

            self.cache[i] = max(nums[i] + dfs(i+2), dfs(i + 1))

            return self.cache[i]
            

        return dfs(0)