import numpy as np

# 1. Create a 1D and 2D array
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[5, 6, 7], [8, 9, 10]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# 2. Reshape and Indexing
reshaped = arr2.reshape(3, 2)
print("Reshaped (3x2):\n", reshaped)
print("Element at (1,2):", arr2[1, 2])

arr1[1:3]             # Elements at index 1 and 2
arr2[:, 1]            # All rows, column 1

# 3. Basic operations
print("Sum:", arr2.sum())
print("Mean:", np.mean(arr2))
print("Max value:", np.max(arr2))

# More useful NumPy features
print("2x3 array of zeros:\n", np.zeros((2, 3)))
print("3x1 array of ones:\n", np.ones((3, 1)))
print("Array with values from 0 to 8 (step 2):", np.arange(0, 10, 2))
print("5 numbers from 0 to 1 (inclusive):", np.linspace(0, 1, 5))

print("arr1 * 2:", arr1 * 2)              # Multiply every element by 2
print("arr1 + arr1:", arr1 + arr1)        # Add arrays element-wise

