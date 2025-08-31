class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # dp[i] will store a list of combinations that sum to i.
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # Base case: one way to make sum 0 (with an empty set).

        # Iterate through each candidate number.
        for candidate in candidates:
            # For each candidate, update the dp table for all sums it can contribute to.
            for i in range(candidate, target + 1):
                # For each combination that sums to i - candidate...
                for prev_combination in dp[i - candidate]:
                    # ...add the current candidate to it to form a new combination for sum i.
                    dp[i].append(prev_combination + [candidate])

        return dp[target]