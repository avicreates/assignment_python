def tsp_held_karp(distance_matrix):
    num_cities = len(distance_matrix)
    
    # The target mask represents all cities visited.
    # For 4 cities, (1 << 4) - 1 = 1111 in binary (decimal 15)
    VISITED_ALL = (1 << num_cities) - 1
    
    # Memoization table: dictionary mapping (mask, current_position) -> min_distance
    memo = {}

    def solve(mask, pos):
        # Base Case: If all cities have been visited, we must return to the start city (0)
        if mask == VISITED_ALL:
            return distance_matrix[pos][0]
        
        # If this exact subproblem state has already been computed, return it
        if (mask, pos) in memo:
            return memo[(mask, pos)]
        
        min_distance = float('inf')
        
        # Try to visit every unvisited city next
        for next_city in range(num_cities):
            # Check if the next_city has NOT been visited yet
            # (1 << next_city) creates a bitmask for just that city
            if (mask & (1 << next_city)) == 0:
                # Update the mask to mark next_city as visited using bitwise OR (|)
                new_mask = mask | (1 << next_city)
                
                # Calculate the cost of moving to the next city + solving the rest of the tour
                new_distance = distance_matrix[pos][next_city] + solve(new_mask, next_city)
                
                # Keep the minimum distance
                min_distance = min(min_distance, new_distance)
                
        # Save the result in our memo table before returning
        memo[(mask, pos)] = min_distance
        return min_distance

    # Start the tour at City 0. The initial mask is (1 << 0) which is 0001 binary (City 0 visited)
    initial_mask = 1
    starting_city = 0
    
    optimal_cost = solve(initial_mask, starting_city)
    return optimal_cost

# --- Example Usage ---
if __name__ == "__main__":
    # 4x4 Distance Matrix
    matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    print("Distance Matrix:")
    for row in matrix:
        print(f"  {row}")
    print()

    min_cost = tsp_held_karp(matrix)
    print(f"Minimum TSP Cost (Held-Karp): {min_cost}")