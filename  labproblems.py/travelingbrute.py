from itertools import permutations

def calculate_route_distance(route, distance_matrix):
    
    total_distance = 0
    num_cities = len(route)
    
     
    for i in range(num_cities - 1):
        from_city = route[i]
        to_city = route[i+1]
        total_distance += distance_matrix[from_city][to_city]
        
     
    last_city = route[-1]
    start_city = route[0]
    total_distance += distance_matrix[last_city][start_city]
    
    return total_distance

def tsp_brute_force(distance_matrix):
 
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    

    start_city = cities[0]
    other_cities = cities[1:]
    
    min_distance = float('inf')
    best_route = None
    
     
    for perm in permutations(other_cities):
       
        current_route = [start_city] + list(perm)
        
         
        current_distance = calculate_route_distance(current_route, distance_matrix)
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = current_route
            
     
    best_route_cycle = best_route + [start_city]
    
    return best_route_cycle, min_distance
 
if __name__ == "__main__":
     
    matrix = [
        [0, 10, 15, 20],  # Distances from City 0
        [10, 0, 35, 25],  # Distances from City 1
        [15, 35, 0, 30],  # Distances from City 2
        [20, 25, 30, 0]   # Distances from City 3
    ]
    
    print("Distance Matrix:")
    for row in matrix:
        print(f"  {row}")
    print()

    optimal_route, shortest_distance = tsp_brute_force(matrix)
    
    print(f"Optimal Route: {' -> '.join(map(str, optimal_route))}")
    print(f"Minimum Distance: {shortest_distance}")