def student_tuple(name, score):
    student_tuple = ()
    for name in name:
        student_tuple += (name, score)
    return student_tuple



student_tuple = 'John', 'Green', 3.3
student_tuple = (student_tuple)
#student_tuple = len(student_tuple)
print(student_tuple)