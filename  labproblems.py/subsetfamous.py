def generate_subsets_bitmask(elements):
    
    
    n = len(elements)
    
    total_subsets = 1 << n
    all_subsets = []
 
    for i in range(total_subsets):
        current_subset = []
        
        
        for j in range(n):
          
            if (i & (1 << j)) > 0:
                current_subset.append(elements[j])
                
        all_subsets.append(current_subset)
        
    return all_subsets

 
if __name__ == "__main__":
    my_set = ['A', 'B', 'C']
    print(f"Original Set: {my_set}\n")
    
    result = generate_subsets_bitmask(my_set)
    
    print(f"Generated {len(result)} subsets:")
     
    for index, subset in enumerate(result):
         
        binary_str = bin(index)[2:].zfill(len(my_set))
        print(f"  Mask {binary_str} -> {subset}")