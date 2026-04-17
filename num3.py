arr = np.array([10, 20, 30, 40])

value = 25
closest = arr[np.abs(arr - value).argmin()]

print(closest)
