def student_tuple(word):
    student_tuple = ()
    for letter in word:
        student_tuple += (letter,)
    return student_tuple


student_name = ("Mary")
result = student_tuple(student_name)
print(result)