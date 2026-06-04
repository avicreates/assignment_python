def knapsack_memoized(weights, profits, capacity):
     
    n = len(profits)
    
    
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
 
    def knapsack_recursive(cap, index):
       
        if index == 0 or cap == 0:
            return 0
 
        if memo[index][cap] != -1:
            return memo[index][cap]
 
        if weights[index - 1] > cap:
            memo[index][cap] = knapsack_recursive(cap, index - 1)
        else:
            # Store the max of including the item vs excluding the item
            include_item = profits[index - 1] + knapsack_recursive(cap - weights[index - 1], index - 1)
            exclude_item = knapsack_recursive(cap, index - 1)
            
            memo[index][cap] = max(include_item, exclude_item)

        return memo[index][cap]

    
    return knapsack_recursive(capacity, n)

 
if __name__ == "__main__":
     
    item_profits = [60, 100, 120]
    item_weights = [10, 20, 30]
    knapsack_capacity = 50

    print("--- 0/1 Knapsack (Memoized Recursion) ---")
    print(f"Weights:  {item_weights}")
    print(f"Profits:  {item_profits}")
    print(f"Capacity: {knapsack_capacity}\n")

    max_profit = knapsack_memoized(item_weights, item_profits, knapsack_capacity)
    print(f"Maximum Profit Achieved: {max_profit}")