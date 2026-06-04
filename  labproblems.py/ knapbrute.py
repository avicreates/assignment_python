def knapsack_brute_force(weights, profits, capacity):
    max_profit = 0
    best_items = []
    used_weight = 0
    n = len(weights)
    for i in range(1 << n):  # Loop through all subsets (2^n)
        subset_profit = 0
        subset_weight = 0
        subset_items = []
        for j in range(n):
            if (i & (1 << j)) > 0:  # If the j-th item is included
                subset_profit += profits[j]
                subset_weight += weights[j]
                subset_items.append(j)
        if subset_weight <= capacity and subset_profit > max_profit:
            max_profit = subset_profit
            best_items = subset_items
            used_weight = subset_weight
    return max_profit, best_items, used_weight
def print_all_subsets(weights, profits, capacity):
     pass
     
if __name__ == "__main__":
    items    = ["Item-1", "Item-2", "Item-3", "Item-4"]
    weights  = [2, 3, 4, 5]
    profits  = [3, 4, 5, 6]
    capacity = 8
 
    print("=" * 60)
    print("0/1 KNAPSACK — BRUTE FORCE")
    print("=" * 60)
    print(f"\nCapacity : {capacity}")
    print(f"\n{'Item':<10} {'Weight':>8} {'Profit':>8}")
    print("-" * 30)
    for name, w, p in zip(items, weights, profits):
        print(f"{name:<10} {w:>8} {p:>8}")
 
        print_all_subsets(weights, profits, capacity)
 
    
    max_profit, best_items, used_weight = knapsack_brute_force(weights, profits, capacity)
 
    print("\n" + "=" * 60)
    print("OPTIMAL SOLUTION")
    print("=" * 60)
    print(f"  Selected items : {[items[i] for i in best_items]}")
    print(f"  Total weight   : {used_weight} / {capacity}")
    print(f"  Max profit     : {max_profit}")
 
    
    n = len(weights)
    print(f"\n  Subsets explored : 2^{n} = {2**n}")
    print(f"  Time complexity  : O(2^n)  →  O(2^{n}) = {2**n} subsets")
    print(f"  Space complexity : O(n)    →  O({n})")
 