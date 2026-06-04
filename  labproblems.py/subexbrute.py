from itertools import combinations

def subset_sum_brute_force(nums, target):
   
    n = len(nums)
    
    
    for r in range(n + 1):
        
        for subset in combinations(nums, r):
             
            if sum(subset) == target:
                print(f"Found matching subset: {subset} -> sum = {target}")
                return True
                
    return False

 
if __name__ == "__main__":
    numbers = [3, 34, 4, 12, 5, 2]
    target_value = 9

    print(f"Input Array: {numbers}")
    print(f"Target Sum: {target_value}\n")

    has_subset = subset_sum_brute_force(numbers, target_value)
    print(f"Does a valid subset exist?: {has_subset}")