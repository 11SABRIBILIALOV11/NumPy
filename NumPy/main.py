import numpy as np

# 1. Creating a NumPy Array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# 2. Creating a 2D Array (Matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", array_2d)

# 3. Generating an array of zeros or ones
zeros_array = np.zeros((3, 3))  # 3x3 matrix of zeros
ones_array = np.ones((2, 4))  # 2x4 matrix of ones
print("\nZeros Array:\n", zeros_array)
print("\nOnes Array:\n", ones_array)

# 4. Array of random numbers
random_array = np.random.rand(3, 3)  # 3x3 matrix with random values between 0 and 1
print("\nRandom Array:\n", random_array)

# 5. Array Operations
array_a = np.array([1, 2, 3, 4, 5])
array_b = np.array([5, 4, 3, 2, 1])
sum_array = array_a + array_b
product_array = array_a * array_b
print("\nSum of Arrays:", sum_array)
print("Product of Arrays:", product_array)

# 6. Matrix Multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print("\nMatrix Product:\n", matrix_product)

# 7. Slicing and Indexing
print("\nFirst element of array_1d:", array_1d[0])
print("First row of array_2d:", array_2d[0, :])

# 8. Reshaping
reshaped_array = np.reshape(array_2d, (3, 2))  # Reshape 2x3 to 3x2
print("\nReshaped Array:\n", reshaped_array)

# 9. Statistical operations
mean_value = np.mean(array_1d)
std_deviation = np.std(array_1d)
print("\nMean of array_1d:", mean_value)
print("Standard Deviation of array_1d:", std_deviation)
