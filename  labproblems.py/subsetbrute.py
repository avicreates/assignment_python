def generate_subsets(elements):
    
    all_subsets = []

    def backtrack(index, current_subset):
         
        if index == len(elements):
            
            all_subsets.append(list(current_subset))
            return
 
        current_subset.append(elements[index])
        backtrack(index + 1, current_subset)
        
        
        current_subset.pop()
 
        backtrack(index + 1, current_subset)

     
    backtrack(0, [])
    return all_subsets

if __name__ == "__main__":
    my_set = ['A', 'B', 'C']
    print(f"Original Set: {my_set}\n")
    
    result = generate_subsets(my_set)
    
    print(f"Generated {len(result)} subsets:")
    for subset in result:
        print(f"  {subset}")