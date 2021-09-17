def merge(left, right) :
    i, j, l1, l2 = 0, 0, len(left), len(right)
    merged = list()
    while i < l1 and j < l2 :
        if left[i] <= right[j] :
            merged.append(left[i])
            i += 1
        else :
            merged.append(right[j])
            j += 1
    while i < l1 :
        merged.append(left[i])
        i += 1
    while j < l2 :
        merged.append(right[j])
        j += 1
    return merged 
    
def merge_sort(arr) :
    if len(arr) == 1 :
        return arr
    i = 0
    j = len(arr) - 1
    mid = i + (j - i)//2
    left = merge_sort(arr[i : mid + 1])
    right = merge_sort(arr[(mid + 1):(j + 1)] )
    return merge(left, right)
    

arr = list(map(int, input().split()))
print(merge_sort(arr))