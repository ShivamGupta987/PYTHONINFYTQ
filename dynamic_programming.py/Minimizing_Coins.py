
def solve(n,x,coins):
    dp = [float('inf')]*(x+1)
    dp[0] = 0
    
    for i in range(1,x+1):
        for j in range(n):
            
            if coins[j] > i or dp[i-coins[j]] == float('inf'):
                continue
            
            
            dp[i] = min(dp[i],dp[i-coins[j]]+1)
    
    if dp[x] != float('inf'):
        return dp[x]
    else:
        return -1
    
n=3
x=11
coins = [1,5,7]

print(solve(n,x,coins))