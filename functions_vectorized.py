import numpy as np


def prod_non_zero_diag(x):

    A = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]) 
    diag = A.diagonal()
    diag_no_0 = diag[diag != 0]
    mult = np.multiply.reduce(diag_no_0)
    print(mult)
    pass


def are_multisets_equal(x, y):
    x = np.array([1, 2, 2, 4])
    y = np.array([4, 2, 1, 2])
    mask = np.isin(x,y)
    print(mask)
    pass


def max_after_zero(x):
    x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
    zero = x==0
    print (x[1:][zero[:-1]].max())
pass


def run_length_encoding(x):
    x = np.array([2, 2, 2, 3, 3, 3, 5])
    uniques = np.unique(x)
    counts = np.unique(x, return_counts=True)
    print(counts)
    pass


def pairwise_distance(x, y):
    distance_matrix([[3,4,6,1]],[[6,7,2,1]])
    pass
