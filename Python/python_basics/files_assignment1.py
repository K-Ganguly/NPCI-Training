# taking inputs for the list : 
entries = list()
entry_set = set() 
entry = "1"
while entry != "exit" :
    entry = list(input("Enter the details of the person (enter 'exit' to stop) : ").split(","))
    if entry[0] == "exit" :
        break
    if len(entry) > 0 and not (tuple(entry[:3]) in entry_set) : 
        entries.append(entry)
        entry_set.add(tuple(entry[:3]))

# writing to the file :
print("The entries to added to the file : ") 
print(repr(entries))
with open("entry_details.txt", "w") as f :
    f.write("Name,Email,Phone_No\n")
    lines = [",".join(entry) for entry in entries]
    lines = [line + "\n" for line in lines ]
    f.writelines(lines)

# reading from the file : 
print("The entries in the file are : ")
entries = list() 
with open("entry_details.txt", "r") as f :
    entries = f.readlines()[1:]
    entries = tuple(map(lambda entry : tuple(entry.split(",")), entries ))



print("The tuples are : ")
print(repr(entries))

