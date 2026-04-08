# Normal way
nums = [1, 2, 3, 4]
squares = []
for i in nums:
    squares.append(i*i)

# Python way
squares = [i*i for i in nums]
print(squares)
