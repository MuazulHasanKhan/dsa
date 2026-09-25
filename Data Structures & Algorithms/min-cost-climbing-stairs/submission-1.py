class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.n = len(cost)
        self.cost = [-1]*self.n

        def dfs(i):
            if i >= self.n:
                return 0
            
            if self.cost[i] != -1:
                return self.cost[i]

            self.cost[i] = cost[i] + min(dfs(i+1), dfs(i +2))


            return self.cost[i]


        return min(dfs(0), dfs(1))


        