marks_data = {
    'Math': [90, 85, 92, 78, 88],
    'Science': [75, 80, 92, 88, 85],
    'English': [88, 90, 82, 95, 78],
}

for subject, marks in marks_data.items():
    total = sum(marks)

    print(f"{subject} - Total: {total}")