class Item:
    def __init__(self, item_id, weight, profit):
        self.item_id = item_id
        self.weight = weight
        self.profit = profit
         
        self.ratio = profit / weight

def fractional_knapsack_greedy(weights, profits, capacity):
    
    
    items = []
    for i in range(len(profits)):
        items.append(Item(item_id=i+1, weight=weights[i], profit=profits[i]))
    
     
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_profit = 0.0
    remaining_capacity = capacity
    selected_items = {}  

    print("--- Greedy Selection Process ---")
    for item in items:
        if remaining_capacity == 0:
            break
            
         
        if item.weight <= remaining_capacity:
            remaining_capacity -= item.weight
            total_profit += item.profit
            selected_items[f"Item {item.item_id}"] = "100%"
            print(f"Took 100% of Item {item.item_id} (Weight: {item.weight}, Profit: {item.profit})")
        
         
        else:
            fraction = remaining_capacity / item.weight
            total_profit += item.profit * fraction
            selected_items[f"Item {item.item_id}"] = f"{fraction * 100:.1f}%"
            print(f"Took {fraction * 100:.1f}% of Item {item.item_id} (Weight taken: {remaining_capacity}, Profit gained: {item.profit * fraction:.2f})")
            remaining_capacity = 0 # Knapsack is now completely full
            break
            
    return total_profit, selected_items

 
if __name__ == "__main__":
    # Problem Setup
    item_weights = [10, 20, 30]
    item_profits = [60, 100, 120]
    knapsack_capacity = 50

    print("--- Fractional Knapsack Problem (Greedy) ---")
    print(f"Weights:  {item_weights}")
    print(f"Profits:  {item_profits}")
    print(f"Capacity: {knapsack_capacity}\n")

    max_profit, item_breakdown = fractional_knapsack_greedy(item_weights, item_profits, knapsack_capacity)
    
    print("\n--- Final Summary ---")
    print(f"Maximum Profit: {max_profit:.2f}")
    print(f"Items Selected: {item_breakdown}")