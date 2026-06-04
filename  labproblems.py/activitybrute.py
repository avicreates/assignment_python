from itertools import combinations

def is_feasible(subset):
    
    sorted_subset = sorted(subset, key=lambda x: x[0])
    
    for i in range(len(sorted_subset) - 1):
         
        if sorted_subset[i+1][0] < sorted_subset[i][1]:
            return False
    return True

def brute_force_activity_scheduling(activities):
     
    n = len(activities)
    max_feasible_set = []

     
    for r in range(1, n + 1):
         
        for subset in combinations(activities, r):
             
            if is_feasible(subset):
                 
                if len(subset) > len(max_feasible_set):
                    max_feasible_set = subset

    return max_feasible_set

 
if __name__ == "__main__":
     
    activities_pool = [
        (1, 4, "Activity A"),
        (3, 5, "Activity B"),
        (0, 6, "Activity C"),
        (5, 7, "Activity D"),
        (3, 9, "Activity E"),
        (5, 9, "Activity F"),
        (6, 10, "Activity G"),
        (8, 11, "Activity H")
    ]

    print("All available activities:")
    for act in activities_pool:
        print(f"  {act[2]}: [{act[0]}, {act[1]})")

    # Run the brute force algorithm
    optimal_schedule = brute_force_activity_scheduling(activities_pool)

    print("\nOptimal Schedule (Maximum non-overlapping activities):")
    for act in optimal_schedule:
        print(f"  {act[2]}: [{act[0]}, {act[1]})")
    print(f"Total activities scheduled: {len(optimal_schedule)}")