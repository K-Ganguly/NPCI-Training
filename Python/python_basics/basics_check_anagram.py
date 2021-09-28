s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")
s3 = input("Enter the third string : ")

char_count_s1 = dict()
for ch in s1 :
    char_count_s1[ch] = char_count_s1.get(ch, 0) + 1

char_count_s2 = char_count_s1.copy()
is_s2_anagram = True
for ch in s2 : 
    if ch in char_count_s2 and char_count_s2[ch] > 0 : 
        char_count_s2[ch] -= 1
        if  char_count_s2[ch] == 0 :
            char_count_s2.pop(ch)
    else :
        is_s2_anagram = False
        break 

char_count_s3 = char_count_s1.copy()
is_s3_anagram = True
for ch in s3 : 
    if ch in char_count_s3 and char_count_s3[ch] > 0 : 
        char_count_s3[ch] -= 1
        if  char_count_s3[ch] == 0 :
            char_count_s3.pop(ch)
    else :
        is_s3_anagram = False
        break 

if is_s2_anagram and is_s3_anagram :
    print("The strings are anagram")
else : 
    print("The strings are NOT anagram")