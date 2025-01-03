
# compettive prograaming question
def count_ways(n):
    Mod = 10**9+7
    dp = [0]*(n+1)
    
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(1,7):
            if i>=j:
                dp[i] = (dp[i]+dp[i-j])%Mod
    return dp[n]

num = int(input())
print(count_ways(num))  # Output: 1
            


# optimized code


def optimised_count_ways(n):
    Mod = 10**9+7
    dp = [0]*(n+1)
    dp[0] = 1
    window_sum = 0
    for i in range(1,n+1):
        window_sum = (window_sum + dp[i-1]) 
        if i > 6:
            window_sum -= dp[i-7]
        dp[i] = window_sum % Mod
            
    return dp[n]
num = int(input())
print(optimised_count_ways(num))
            
