original_list = [1, 2, 3, 4, 5, 6, 7]

def find_subgroups(original_list):
    def helper(subgroup, start):
        if start == len(original_list):
            all_subgroups.append(list(subgroup))
            return
        
        # Include the current element in the subgroup
        subgroup.append(original_list[start])
        helper(subgroup, start + 1)
        
        # Exclude the current element from the subgroup
        subgroup.pop()
        helper(subgroup, start + 1)
    
    all_subgroups = []
    helper([], 0)
    
    # Filter out the subgroups of all possible sizes that together form the original list
    result = []
    for size in range(1, len(original_list) + 1):
        for subgroup in all_subgroups:
            if len(subgroup) == size:
                result.append(subgroup)
    
    return result

def recreate_original_list(subgroups, original_list):
    original_set = set(original_list)
    
    def backtrack(start, current_combination, used_elements):
        if used_elements == original_set:
            valid_combinations.append(list(current_combination))
            return
        
        if start >= len(subgroups):
            return
        
        for i in range(start, len(subgroups)):
            subgroup_set = set(subgroups[i])
            if not subgroup_set & used_elements:  # Ensure no overlap with already used elements
                backtrack(i + 1, current_combination + [subgroups[i]], used_elements | subgroup_set)
    
    valid_combinations = []
    backtrack(0, [], set())
    
    return valid_combinations

subgroups = find_subgroups(original_list)
valid_combinations = recreate_original_list(subgroups, original_list)

print("All Subgroups:")
for subgroup in subgroups:
    print(subgroup)

print("\nValid Combinations to Recreate Original List:")
for combination in valid_combinations:
    print(combination)
