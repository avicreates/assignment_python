def job_sequencing_greedy(jobs):
     
    sorted_jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    schedule = [None] * (max_deadline + 1)
    
    total_profit = 0
    scheduled_jobs_count = 0
 
    for job in sorted_jobs:
        job_id, deadline, profit = job
        
        
        for slot in range(deadline, 0, -1):
            if schedule[slot] is None:
                
                schedule[slot] = job_id
                total_profit += profit
                scheduled_jobs_count += 1
                break  
                
     
    final_sequence = [job for job in schedule if job is not None]
    
    return final_sequence, total_profit

 
if __name__ == "__main__":
     
    job_pool = [
        ('Job A', 2, 100),
        ('Job B', 1, 19),
        ('Job C', 2, 27),
        ('Job D', 1, 25),
        ('Job E', 3, 15)
    ]

    print("Available Jobs:")
    for j in job_pool:
        print(f"  {j[0]} -> Deadline: {j[1]}, Profit: ${j[2]}")
    print()

    sequence, max_profit = job_sequencing_greedy(job_pool)
    
    print(f"Optimal Job Sequence: {sequence}")
    print(f"Maximum Profit Earned: ${max_profit}")