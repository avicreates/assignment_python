from itertools import permutations

def evaluate_schedule(job_order):
    
    current_time = 0
    total_profit = 0
    scheduled_jobs = []
    
    for job in job_order:
        job_id, deadline, profit = job
         
        if current_time + 1 <= deadline:
            current_time += 1
            total_profit += profit
            scheduled_jobs.append(job_id)
         
            
    return scheduled_jobs, total_profit

def job_sequencing_brute_force(jobs):
    
    max_profit = -1
    best_sequence = []
    
     
    for perm in permutations(jobs):
        scheduled_jobs, profit = evaluate_schedule(perm)
        
         
        if profit > max_profit:
            max_profit = profit
            best_sequence = scheduled_jobs
            
    return best_sequence, max_profit

 
if __name__ == "__main__":
     
    job_pool = [
        ('Job A', 2, 100),
        ('Job B', 1, 19),
        ('Job C', 2, 27),
        ('Job D', 1, 25),
        ('Job E', 3, 15)
    ]
    
    print("Available Jobs:")
    for job in job_pool:
        print(f"  {job[0]} -> Deadline: {job[1]}, Profit: ${job[2]}")
    print()

    optimal_jobs, total_profit = job_sequencing_brute_force(job_pool)
    
    print(f"Optimal Job Sequence: {optimal_jobs}")
    print(f"Maximum Profit Earned: ${total_profit}")