def is_subset_sum_dp(numbers, target):
     
    n = len(numbers)
    
   
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
     
    for i in range(n + 1):
        dp[i][0] = True
        
     
    for i in range(1, n + 1):
        current_num = numbers[i - 1]
        for j in range(1, target + 1):
             
            
            dp[i][j] = dp[i - 1][j]
             
            if j >= current_num:
                
                dp[i][j] = dp[i][j] or dp[i - 1][j - current_num]
                
    return dp[n][target]

 
if __name__ == "__main__":
    items = [3, 34, 4, 12, 5, 2]
    target_sum = 9
    
    print(f"Given Set: {items}")
    print(f"Target Sum: {target_sum}")
    
    exists = is_subset_sum_dp(items, target_sum)
    print(f"Does a subset exist? {exists}") 
    