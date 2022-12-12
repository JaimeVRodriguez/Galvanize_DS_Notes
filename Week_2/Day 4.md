## Numpy
***

### Basics

Standard import of numpy
`import numpy as np`

Creating a numpy array
```
my_lst_ndarray = np.arry([1, 2, 3, 4, 5])
my_tuple_ndarray = np.array((1, 2, 3, 4, 5), np.int32)
```

Examples
![[numpy_basics.ipynb]]

### Arithmetic
![[arithmetic.ipynb]]

### Reshaping/Transposing
![[reshaping.ipynb]]

### Indexing


### Loading CSV
https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html
`numpy.loadtxt()`

need a delimiter - how the items are split
`numpy.loadtxt(delimiter=",")`