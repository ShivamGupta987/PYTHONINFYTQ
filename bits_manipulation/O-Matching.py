MOD = 10**9 + 7

def count_ways(N, compatibility):
    dp = [0] * (1 << N)
    dp[0] = 1  # base case: No pair created yet.
    
    for mask in range(1 << N):  # sabhi masks ke liye iterate karte hain
        man = bin(mask).count('1')  # kitne men paired ho chuke hain
        for woman in range(N):
            if (mask & (1 << woman)) == 0 and compatibility[man][woman] == 1:
                new_mask = mask | (1 << woman)  # new pair banate hain
                dp[new_mask] = (dp[new_mask] + dp[mask]) % MOD

    return dp[(1 << N) - 1]  # sabhi men paired ho gaye hain

# Example input: N = 3
compatibility = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]

print(count_ways(3, compatibility))  # Expected output: number of ways modulo 10^9 + 7
