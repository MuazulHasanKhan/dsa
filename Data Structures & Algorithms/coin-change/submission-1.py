class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
       
       # at every step we n choices
       # return conditions
            # if target < 0, return
            # if traget == 0, compare self.cmin with current c 
        self.mincnt = float('inf')
        self.dp = {0: 0}
        def solution(target):
            if target in self.dp:
                return self.dp[target]

            if target <0:
                return float('inf')

            curr_min = float('inf')
            for i in coins:
                curr_min = min(curr_min, 1 + solution(target - i))
            
            self.dp[target] = curr_min
                    

            return self.dp[target]

        res = solution(amount)
        if res == float('inf'):
            return -1

        return res
