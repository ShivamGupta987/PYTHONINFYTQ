
def solve(n):
    dp = [float('inf')]*(n+1)
    dp[0]=0
    
    for i in range(1,n):
        temp= i 
        while temp:
            d = temp%10
            dp[i] = min(dp[i],1+dp[i-d])
            d = d//10
    return dp[n]
print(solve(25))