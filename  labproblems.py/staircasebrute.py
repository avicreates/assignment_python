def climb_stairs_brute_force(n):
     
    if n == 0:
        return 1
        
    
    if n < 0:
        return 0
        
 
    return climb_stairs_brute_force(n - 1) + climb_stairs_brute_force(n - 2)

 
if __name__ == "__main__":
    total_stairs = 4
    
    print(f"Total stairs to climb: {total_stairs}")
    
    ways = climb_stairs_brute_force(total_stairs)
    print(f"Number of distinct ways to reach the top: {ways}")