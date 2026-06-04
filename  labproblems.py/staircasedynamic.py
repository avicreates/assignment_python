def climb_stairs_dp(n):
    """
    Calculates the total number of distinct ways to climb n stairs
    using Bottom-Up Dynamic Programming (Linear Space).
    """
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

     
    dp = [0] * (n + 1)
    
     
    dp[1] = 1
    dp[2] = 2

     
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

if __name__ == "__main__":
    total_stairs = 5
    print(f"Total stairs: {total_stairs}")
    print(f"Number of ways (DP): {climb_stairs_dp(total_stairs)}")