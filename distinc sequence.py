class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp[c] = number of distinct subsequences ending with character c
        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            # Every existing distinct subsequence can append ch,
            # plus the subsequence consisting only of ch.
            total = 1 + sum(dp)
            dp[i] = total % MOD

        return sum(dp) % MOD
