class Solution:
    def numDecodings(self, s: str) -> int:
        dict_ = {len(s): 1}

        def dfs_memo(i):
            if i in dict_:
                return dict_[i]

            if s[i] == "0":
                return 0

            dict_[i] = dfs_memo(i+1)

            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                dict_[i] += dfs_memo(i+2)

            return dict_[i] 

        return dfs_memo(0)