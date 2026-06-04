def greedy_coin_change(coins, amount):
     
     
    sorted_coins = sorted(coins, reverse=True)
    
    coin_count = 0
    selected_coins = {}  

    for coin in sorted_coins:
        if amount == 0:
            break
            
        if amount >= coin:
             
            count = amount // coin
            
            
            amount %= coin
            coin_count += count
            
             
            selected_coins[coin] = count

     
    if amount > 0:
        return None, "Exact change cannot be made with these denominations."
        
    return coin_count, selected_coins

 
if __name__ == "__main__":
    
    indian_coins_notes = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    
    target_amount = 868  # e.g., ₹868
    
    print(f"Available Denominations: {indian_coins_notes}")
    print(f"Target Amount: ₹{target_amount}\n")
    
    total_coins, breakdown = greedy_coin_change(indian_coins_notes, target_amount)
    
    if total_coins is not None:
        print(f"Minimum notes/coins required: {total_coins}")
        print("Breakdown:")
        for coin, count in breakdown.items():
            print(f"  ₹{coin} x {count}")
    else:
        print(breakdown)