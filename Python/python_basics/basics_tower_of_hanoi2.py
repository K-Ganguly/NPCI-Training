lines = int(input("Enter the number of lines : "))
step = int(input("Enter the step size : "))
value = 1
first_value = 1
matrix = list()


# Part 1 : 
print("\n\nPart 1 : \n")
for i in range(lines) :
    row = list()
    print("\t" * (lines - i - 1), end = "")
    value = first_value
    for _ in range(i + 1) :
        row.append(value)
        print(value, end = "\t\t")
        value += 1
    print()
    matrix.append(row)
    first_value += step


# Part 2 : 
print("\n\nPart 2 :")
row_sum = 0
row_sums = list()
for row_no, row in enumerate(matrix) :
    print("Row {} : ".format(row_no + 1), end = " ")
    for i, element in enumerate(row) : 
        if i == len(row) - 1 :
            print(element , end = " = ")
        else : 
            print(element, end = " + ")
        row_sum += element
    print(row_sum)
    row_sums.append(row_sum)

row_print = ""
sum_print = "" 
final_sum = 0
for i, row_sum in enumerate(row_sums) : 
    row_print += ("Row {}".format(i + 1))
    sum_print += str(row_sum)
    final_sum += row_sum
    if i < len(row_sums) - 1 :
        row_print += " + "
        sum_print += " + "
    else : 
        row_print += " = "
        sum_print += " = "

final_s = row_print + sum_print + str(final_sum)
print("Row {} : {} ".format(str(len(matrix)+1), final_s))

# Part 3 : Creating the matrix
print("\n\nPart 3 : ") 
for row in matrix : 
    while len(row) < lines : 
        row.append(0)
matrix.reverse()
for row in matrix : 
    print(row)

# Part 4 : Finding square of the matrix 
print("\n\nPart 4  : ")
sq_matrix = [[0 for _ in range(len(matrix[0]))]
    for _ in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        sq_matrix[i][j] = 0
        for k in range(len(matrix)):                
            sq_matrix[i][j] += matrix[i][k] * matrix[k][j]

for row in matrix : 
    print(row)