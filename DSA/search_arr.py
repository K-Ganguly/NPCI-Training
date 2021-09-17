def search(arr, key, case) :
    if case == 1 :
        for i, num in enumerate(arr) :
            if num == key  :
                return i
    if case == 2 :
        idx = list()
        for i, num in enumerate(arr) :
            if num == key :
                idx.append(i)
        return idx

arr = list(map(int, input().split()))
key = int(input())
case = int(input())
print(search(arr, key, case))