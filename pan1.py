students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["A", "B", "C"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [85, 90, 78]
})

merged = pd.merge(students, marks, on="ID")

print(merged)
