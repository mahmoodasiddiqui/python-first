import numpy as np

#create 100,000 numbers using python range
to_square = range(100000)
# time how long it takes to repeatedly square them all
squares(to_square)


# now lets do this with a numpy array
array_to_square = np.arange(0, 100000)
# and time using a vectorized operation
array_to_square ** 2