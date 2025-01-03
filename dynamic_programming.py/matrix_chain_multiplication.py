
def matrix_multiplication(arr,n):
    dp=[[0  for _ in range(n)] for _ in range(n) ]
    
    for chain_len in range(2,n):
        for i in range(1,n-chain_len+1):
            j = i+chain_len-1
            dp[i][j] = float('inf')
            
            for k in range(I,j):
                cost = dp[i][k] + dp[k+1][j] + arr[i-j]*arr[k]*arr[j]
                dp[i][j] = min(dp[i][j],cost)
                
    return dp[1][n-1]

arr=[40,10,30,11,19]
n = len(arr)
print(matrix_multiplication(arr,n))