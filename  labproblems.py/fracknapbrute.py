def fractional_knapsack_brute_force(weights, profits, capacity, step=0.1):
    
    n = len(profits)
    best_profit = 0.0
 
    steps_count = int(1 / step) + 1
    possible_fractions = [round(i * step, 10) for i in range(steps_count)]
    def evaluate_combinations(item_index, current_weight, current_profit):
        nonlocal best_profit

         
        if item_index == n:
            if current_weight <= capacity:
                best_profit = max(best_profit, current_profit)
            return

         
        if current_weight > capacity:
            return

         
        for fraction in possible_fractions:
            next_weight = current_weight + (weights[item_index] * fraction)
            next_profit = current_profit + (profits[item_index] * fraction)

            evaluate_combinations(item_index + 1, next_weight, next_profit)
 
    evaluate_combinations(0, 0.0, 0.0)
    return best_profit


def fractional_knapsack_greedy(weights, profits, capacity):
    """
    The mathematically optimal solution using the Greedy approach.
    """
    
    items = []
    for i in range(len(profits)):
        items.append(
            {
                "weight": weights[i],
                "profit": profits[i],
                "ratio": profits[i] / weights[i],
            }
        )
    items.sort(key=lambda x: x["ratio"], reverse=True)

    total_profit = 0.0
    current_weight = 0

    for item in items:
        if current_weight + item["weight"] <= capacity:
             
            current_weight += item["weight"]
            total_profit += item["profit"]
        else:
             
            remaining_capacity = capacity - current_weight
            total_profit += item["ratio"] * remaining_capacity
            break

    return total_profit


 
if __name__ == "__main__":
    # Problem Configuration
    item_weights = [10, 20, 30]
    item_profits = [60, 100, 120]
    knapsack_capacity = 50

    print("--- Fractional Knapsack Analysis ---")
    print(f"Weights:  {item_weights}")
    print(f"Profits:  {item_profits}")
    print(f"Capacity: {knapsack_capacity}\n")

     
    exact_solution = fractional_knapsack_greedy(
        item_weights, item_profits, knapsack_capacity
    )
    print(f"Greedy Strategy (Exact Max Profit):  {exact_solution:.2f}")

     
    approx_10_pct = fractional_knapsack_brute_force(
        item_weights, item_profits, knapsack_capacity, step=0.1
    )
    print(f"Brute Force (Step 0.1 / 10% blocks): {approx_10_pct:.2f}")

     
    approx_1_pct = fractional_knapsack_brute_force(
        item_weights, item_profits, knapsack_capacity, step=0.01
    )
    print(f"Brute Force (Step 0.01 / 1% blocks): {approx_1_pct:.2f}")