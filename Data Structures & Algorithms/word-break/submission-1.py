class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {len(s): True}
        
        def utility(i):

            if i in dp:
                return dp[i]
            
            dp[i] = False
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    if utility(i + len(w)):
                        dp[i] = True
                        

            return dp[i]


        return utility(0)