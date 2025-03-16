#. Iterate over a 2D NumPy array row-wise and column-wise using nditer(). 
import numpy as np
array=np.arange(1,10).reshape(3,3)
# for row in np.nditer(arr):
#     print(f"Row index:")
# Iterate row-wise (default behavior)
print("Row-wise iteration:")
for idx, value in np.ndenumerate(array):
    print(f"Row index: {idx}, Value: {value}")

# Column-wise iteration using transpose (T) for nditer
print("\nColumn-wise iteration:")
for idx, value in np.ndenumerate(array.T):  # Transpose to iterate column-wise
    print(f"Column index: {idx}, Value: {value}")