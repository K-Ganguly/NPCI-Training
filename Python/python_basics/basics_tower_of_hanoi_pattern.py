lines = int(input("Enter the number of lines : "))
step = int(input("Enter the step size : "))
value = 1

for i in range(lines) :
    print("  " * (lines - i - 1), end = "")
    for _ in range(i + 1) :
        print(value, end = "   ")
    print()
    value += step
value = 1
print("\n")
for line_num in range(1, lines + 1) :
    print(f"Line {(line_num + 1)} : {value}s : {value} * {line_num} ")
    value += step 
