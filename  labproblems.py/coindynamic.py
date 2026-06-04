def coin_change_dp(coins, amount):
     
    dp = [float('inf')] * (amount + 1)
    
    
    dp[0] = 0
    
 
    for i in range(1, amount + 1):
        for coin in coins: 
            if i - coin >= 0:
                 
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    
    return dp[amount] if dp[amount] != float('inf') else -1

 
if __name__ == "__main__":
    
    coin_denominations = [1, 3, 4]
    target_amount = 6

    print(f"Available Coins: {coin_denominations}")
    print(f"Target Amount: {target_amount}")
    
    min_coins = coin_change_dp(coin_denominations, target_amount)
    
    if min_coins != -1:
        print(f"Minimum coins required (DP): {min_coins}")
    else:
        print("It's impossible to make the target amount with given coins.")