
def sort_dict(nums_dict) :

    # helper functions 
    def merge(left_keys, left_vals, right_keys, right_vals) :
        i, j = 0, 0
        merged_keys = list()
        merged_vals = list()
        while i < len(left_keys) and j < len(right_keys) :
            if left_vals[i] <= right_vals[j] :
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

print("Enter the number of the elements of the dictionary : ")
n = int(input())
print("Enter the items of the dictionary in key-value order : ")
num_dict = dict()
for _ in range(n) :
    key, value = input().split()
    num_dict[key] = value 

print("Before Sorting : ")
print(num_dict)
sorted_dict = sort_dict(num_dict)
print("After Sorting : ")
print(sorted_dict)