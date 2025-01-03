# 518 coin change 2 leetcode


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up approach 

        dp=[0]*(amount+1)

        dp[0] = 1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]+=dp[i-coin]
        return dp[amount] if dp[amount]>0 else 0




# 198 house robber class Solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        dp=[0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
    
    
# 322 coins
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up approach 

        dp=[amount+1]*(amount+1)

        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]=min(dp[i],dp[i-coin]+1)

        return dp[amount] if dp[amount] != amount+1 else -1
        




# 63 leetcode unique path 2
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]==1:
            return 0

        dp = [[0]*n for _ in range(m)]
        dp[0][0]=1

        for j in range(1,n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j]==0 else 0

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0]==0 else 0
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                else:
                     dp[i][j]= 0
        return dp[m-1][n-1]


# 96 leetcod eunique binary search tree
class Solution:
    def numTrees(self, n: int) -> int:
        self.table = [-1] * (n + 1)
        self.table[0] = 1  # Base case

        return self.numTreeRec(n)

    def numTreeRec(self, n: int) -> int:
        # Return cached value if already computed
        if self.table[n] != -1:
            return self.table[n]

        # Compute total number of unique BSTs
        total = 0
        for m in range(n):
            total += self.numTreeRec(m) * self.numTreeRec(n - 1 - m)

        self.table[n] = total  # Store result in cache
        return total



