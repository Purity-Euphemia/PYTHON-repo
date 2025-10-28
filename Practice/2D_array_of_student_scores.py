
student_scores = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
]

print("All student scores:")
for row_index, score_row in enumerate(student_scores):
    for col_index, score in enumerate(score_row):
        print(f"Student {row_index+1}, Exam {col_index+1}: {score}")
