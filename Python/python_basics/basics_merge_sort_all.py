# for sorting dictionaries 
def sort_dict(nums_dict) :

    # helper functions 
    def merge(left_keys, left_vals, right_keys, right_vals) :
        i, j = 0, 0
        merged_keys = list()
        merged_vals = list()
        while i < len(left_keys) and j < len(right_keys) :
            if left_keys[i] <= right_keys[j] :
                merged_keys.append(left_keys[i])
                merged_vals.append(left_vals[i])
                i += 1
            else : 
                merged_keys.append(right_keys[j])
                merged_vals.append(right_vals[j])
                j += 1
        while i < len(left_keys) :
            merged_keys.append(left_keys[i])
            merged_vals.append(left_vals[i])
            i += 1
        while j < len(right_keys) :
            merged_keys.append(right_keys[j])
            merged_vals.append(right_vals[j])
            j += 1
        return merged_keys, merged_vals


    def merge_sort(num_keys, num_vals) :
        if len(num_keys) == 1 :
            return num_keys, num_vals
        else :
            l = len(num_keys)
            mid = l // 2
            left_keys, left_vals = merge_sort(num_keys[:mid], num_vals[:mid])
            right_keys, right_vals = merge_sort(num_keys[mid:], num_vals[mid:])
            merged_keys, merged_vals = merge(left_keys, left_vals, right_keys, right_vals)
        return merged_keys, merged_vals
    
    # converting dictionary items to list of keys and values separately 
    def dict_to_list(num_dict) :
        num_dict_keys = list()
        num_dict_vals = list() 
        for key, val in num_dict.items() :
            num_dict_keys.append(key)
            num_dict_vals.append(val)
        return num_dict_keys, num_dict_vals

    num_keys, num_vals = dict_to_list(nums_dict)
    sorted_keys, sorted_vals = merge_sort(num_keys, num_vals)
    sorted_dict = {key : val for key, val in zip(sorted_keys, sorted_vals)}
    return sorted_dict

# for sorting elements 
def sort_nums(nums) :

    def merge(left, right) :
        i, j = 0, 0
        merged = list()
        while i < len(left) and j < len(right) :
            if left[i] <= right[j] :
                merged.append(left[i])
                i += 1
            else : 
                merged.append(right[j])
                j += 1
        while i < len(left) :
            merged.append(left[i])
            i += 1
        while j < len(right) :
            merged.append(right[j])
            j += 1
        return merged

    def merge_sort(nums) :
        if len(nums) == 1 :
            return [nums[0]]
        else :
            l = len(nums)
            mid = l // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            merged_nums = merge(left, right)
        return merged_nums
    nums_type = type(nums)
    nums = list(nums)
    sorted_nums = merge_sort(nums)
    if type == set : 
        sorted_nums = set(sorted_nums)
    elif type == list :
        pass 
    elif type == tuple : 
        sorted_nums = tuple(sorted_nums)
    return sorted_nums

def sorted_elements(elements) :
    if type(elements) == dict :
        sorted_nums = sort_dict(elements)
        return sorted_nums
    else :
        sorted_nums = sort_nums(elements)
        return sorted_nums



choice = int(input("\n\n1. Dictionary \n2. Set \n3. Tuple \n4. List\n"))
if choice == 1 : 
    print("Enter the number of the elements of the dictionary : ")
    n = int(input())
    print("Enter the items of the dictionary in key-value order : ")
    num_dict = dict()
    for _ in range(n) :
        key, value = input().split()
        num_dict[key] = value 
else : 
    if choice == 2 :
        elements = set(input("Enter the elements of the set : ").split())
    elif choice == 3 : 
        elements = tuple(input("Enter the elements of the tuple : ").split())
    elif choice == 4 :
        elements = list(input("Enter the elements of the list : ").split())
    
print("Before Sorting : {}".format(elements))
sorted_elements = sorted_elements(elements)
print("After Sorting : {}".format(sorted_elements))
