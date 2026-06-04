def next_fit(items, capacity):
     
    bins = [[]]
    current_bin_weight = 0
    
    for item in items:
        if current_bin_weight + item <= capacity:
            bins[-1].append(item)
            current_bin_weight += item
        else:
            # Open a new bin and switch context entirely to it
            bins.append([item])
            current_bin_weight = item
            
    return bins


def first_fit(items, capacity):
     
    bins = []
    
    for item in items:
        placed = False
         
        for b in bins:
            if sum(b) + item <= capacity:
                b.append(item)
                placed = True
                break
         
        if not placed:
            bins.append([item])
            
    return bins


def best_fit(items, capacity):
     
    bins = []
    
    for item in items:
        best_bin_idx = -1
        min_remaining_space = capacity + 1
        
         
        for idx, b in enumerate(bins):
            remaining_space = capacity - sum(b)
            if item <= remaining_space < min_remaining_space:
                best_bin_idx = idx
                min_remaining_space = remaining_space
                
         
        if best_bin_idx != -1:
            bins[best_bin_idx].append(item)
        else:
            
            bins.append([item])
            
    return bins


def first_fit_decreasing(items, capacity):
     
    sorted_items = sorted(items, reverse=True)
    return first_fit(sorted_items, capacity)


 
if __name__ == "__main__":
    item_list = [4, 8, 1, 4, 2, 1, 7, 3, 5]
    bin_capacity = 10

    print(f"Items to pack: {item_list}")
    print(f"Max Bin Capacity: {bin_capacity}\n")
 
    heuristics = {
        "Next Fit (NF)": next_fit,
        "First Fit (FF)": first_fit,
        "Best Fit (BF)": best_fit,
        "First Fit Decreasing (FFD)": first_fit_decreasing
    }

    for name, func in heuristics.items():
        result = func(item_list, bin_capacity)
        print(f"{name}:")
        print(f"  Total Bins: {len(result)}")
        print(f"  Bins Configuration: {result}")