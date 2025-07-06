def student_tuple_index(name):
    student_tuple = ()
    for count in range(len(name)):
        student_tuple += ((count, name[count]),)
    return student_tuple



student_tuple = ('Mary')
result = student_tuple_index(student_tuple)
print(result)