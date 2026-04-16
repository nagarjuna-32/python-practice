arr = np.array([1, 2, 3, 2, 4, 5, 1])

unique, counts = np.unique(arr, return_counts=True)

duplicates = unique[counts > 1]
print(duplicates)
