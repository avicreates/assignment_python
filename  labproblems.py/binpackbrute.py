def bin_packing_brute_force(items, bin_capacity):
     
    n = len(items)
     
    best_bins_count = n 
    
    
    bins_remaining_capacity = [bin_capacity] * n

    def backtrack(item_index, current_bins_used):
        nonlocal best_bins_count
        
         
        if current_bins_used >= best_bins_count:
            return

         
        if item_index == n:
            best_bins_count = min(best_bins_count, current_bins_used)
            return

        current_item_weight = items[item_index]

         
        for bin_id in range(min(current_bins_used + 1, n)):
            
             
            if bins_remaining_capacity[bin_id] >= current_item_weight:
                
                 
                is_new_bin = (bin_id == current_bins_used)
                
                 
                bins_remaining_capacity[bin_id] -= current_item_weight
                
                 
                next_bins_used = current_bins_used + 1 if is_new_bin else current_bins_used
                backtrack(item_index + 1, next_bins_used)
                
                 
                bins_remaining_capacity[bin_id] += current_item_weight

     
    backtrack(0, 0)
    return best_bins_count

 
if __name__ == "__main__":
    # Item weights
    item_list = [4, 8, 1, 4, 2, 1]
    capacity = 10

    print(f"Items to pack: {item_list}")
    print(f"Max Bin Capacity: {capacity}\n")

    min_bins = bin_packing_brute_force(item_list, capacity)
    print(f"Minimum number of bins required (Brute Force): {min_bins}")