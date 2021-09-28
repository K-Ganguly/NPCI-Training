elements = set(map(int, input("Enter the elements of the set : ").split()))

def merge(left, right) :
    i, j = 0, 0
    merged = list()
    while i < len(left) and j < len(right) :
        if left[i] > right[j] :
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

print("Before Sorting : {}".format(elements))
sorted_elements = set(merge_sort(list(elements)))
print("After Sorting : {}".format(sorted_elements))