confusion_matrix = [
    [50, 2],
    [3, 45]
]

correct = confusion_matrix[0][0] + confusion_matrix[1][1]
total = sum(sum(row) for row in confusion_matrix)
accuracy = correct / total * 100
print(f"Accuracy: {accuracy:.2f}%")
