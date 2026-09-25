class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.memory = [-1]*(len(nums) -  1)

        def dfs(i, nums_):
            if i >= len(nums) - 1:
                return 0

            if self.memory[i] != -1:
                return self.memory[i]

            self.memory[i] = max(nums_[i] + dfs(i +2, nums_), dfs(i+1, nums_))

            return self.memory[i]

        excluding_first = dfs(0, nums[1:])
        self.memory = [-1]*(len(nums) - 1)
        excluding_last = dfs(0, nums[:-1])

        return max(excluding_first, excluding_last)