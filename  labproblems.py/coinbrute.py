def coin_change_brute_force(coins, amount):
     
    
    if amount == 0:
        return 0
    
     
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    
     
    for coin in coins:
        
        result = coin_change_brute_force(coins, amount - coin)
        
         
        if result != float('inf'):
             
            min_coins = min(min_coins, result + 1)
            
    return min_coins


if __name__ == "__main__":
    coin_denominations = [1, 3, 4]
    target_amount = 6

    print(f"Available Coins: {coin_denominations}")
    print(f"Target Amount: {target_amount}")
    
    min_tokens = coin_change_brute_force(coin_denominations, target_amount)
    
    if min_tokens != float('inf'):
        print(f"Minimum coins required: {min_tokens}")
    else:
        print("It's impossible to make the target amount with given coins.")