num_students = int(input())
students = list()
passed = list()
distinction = list() 
first_div = list()
second_div = list()
re_appear = list()
failed = list()

for i in range(num_students) :
    roll_no = i + 1
    marks_list = list(map(int, input("Enter the marks for Physics, Chemistry and Mathematics : ").split()))
    count = 0 
    for marks in marks_list :
        if marks < 50 : 
            count += 1
    if count > 1 :
        failed.append(roll_no)
    elif count == 1 :
        re_appear.append(roll_no)
    else : 
        passed.append(roll_no)
        avg_marks = sum(marks_list)/3
        if ( avg_marks >= 80) :
            distinction.append(roll_no)
        elif (avg_marks >= 60) :
            first_div.append(roll_no)
        else : 
            second_div.append(roll_no)

print("Class Performance Details : ")
print("Percentage of Students failed : ", (len(failed)/num_students) * 100)
print("Percentage of Students reappearing : ", (len(re_appear)/num_students) * 100)
print("Percentage of Students passed : ", (len(passed)/num_students) * 100)
print("Percentage of Students in Distinction : ", (len(distinction)/num_students) * 100)
print("Percentage of Students in First Division : ", (len(first_div)/num_students) * 100)
print("Percentage of Students in Second Division : ", (len(second_div)/num_students) * 100)