def greedy_activity_scheduling(activities):
     
     
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected_activities = []
    
     
    if sorted_activities:
        first_activity = sorted_activities[0]
        selected_activities.append(first_activity)
        last_finish_time = first_activity[1]
    else:
        return []

     
    for i in range(1, len(sorted_activities)):
        current_activity = sorted_activities[i]
        start_time = current_activity[0]
        
 
        if start_time >= last_finish_time:
            selected_activities.append(current_activity)
             
            last_finish_time = current_activity[1]
            
    return selected_activities

 
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

     
    optimal_schedule = greedy_activity_scheduling(activities_pool)

    print("\nOptimal Schedule (Greedy Selection by Finish Time):")
    for act in optimal_schedule:
        print(f"  {act[2]}: [{act[0]}, {act[1]})")
    print(f"Total activities scheduled: {len(optimal_schedule)}")