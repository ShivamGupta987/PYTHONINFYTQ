def max_score_rabbits(compatibility):
    N = len(compatibility)  # Number of rabbits
    
    # Total bitmasks hote hain 2^N
    dp = [0] * (1 << N)  # DP array jo maximum score har group ke liye rakhega.
    
    # Group ke score ko store karenge jisme ek se zyada rabbits hain.
    group_score = [0] * (1 << N)
    
    # Precompute score for each group
    for mask in range(1 << N):  
        for i in range(N):     
            if mask & (1 << i):  # Check karte hain ki Rabbit 'i' group mein hai ya nahi
                for j in range(i + 1, N):  # Rabbit 'j' bhi usi group mein ho toh score add hoga
                    if mask & (1 << j):    # Check karte hain ki Rabbit 'j' bhi group mein hai
                        group_score[mask] += compatibility[i][j]  # i aur j ke beech ka compatibility score add karte hain
    
    # Ab DP table fill karte hain taki maximum score har bitmask ke liye mil sake.
    for mask in range(1 << N):  # Sab possible masks ke liye iterate karte hain
        submask = mask  # Har group ke liye subgroups dekhte hain
        while submask:  # Subgroups ke liye check karte hain
            dp[mask] = max(dp[mask], dp[mask ^ submask] + group_score[submask]) 
            submask = (submask - 1) & mask  # Next subgroup ke liye shift karte hain
    
    # Answer DP table ka last mask (111...N bits) hoga jisme sabhi rabbits same group mein hain.
    return dp[(1 << N) - 1]  # Final answer, jo sabhi rabbits ek group mein hone par milega.

# Example usage:
compatibility = [
    [0, 2, 3],  
    [2, 0, 1],  
    [3, 1, 0]   
]

result = max_score_rabbits(compatibility)
print("Maximum possible score:", result)
