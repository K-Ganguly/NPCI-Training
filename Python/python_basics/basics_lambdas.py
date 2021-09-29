elements_list = list()
elem_dict = dict()

# Adding element to the list : 
def add_element() :
    elem = int(input("Enter the element you want to add : "))
    elements_list.append(elem)
    return "After adding {}, List is {} ".format(elem, elements_list)

# Creating a dictionary from the list : 
def create_dict() :
    if len(elements_list) < 2 :
        return "List is too short to be made a dictionary"
    else : 
        for num in elements_list : 
            elem_dict[num] = elem_dict.get(num, 0) + 1
        return "Created Dictionary from List : {} is \n{}".format(elements_list, elem_dict)


# Sort the dict by value 
def sort_dict() :
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

    num_keys, num_vals = dict_to_list(elem_dict)
    sorted_keys, sorted_vals = merge_sort(num_keys, num_vals)
    sorted_dict = {key : val for key, val in zip(sorted_keys, sorted_vals)}
    return "Dictionary Sorted by Value : {}".format(sorted_dict)

def exit_menu() : 
    return "Exiting ........... "

choice = 1
while choice != 4 : 
    choice = int(input("\n\n1. Add a new element to the list\n2. Create a dictionary from the list\n3. Sort the dictionary in descending order based on value\n4.Exit\n"))
    if choice == 1 :
        print(add_element())
    elif choice == 2 : 
        print(create_dict())
    elif choice == 3 :
        print(sort_dict())
    else : 
        print(exit_menu())
    