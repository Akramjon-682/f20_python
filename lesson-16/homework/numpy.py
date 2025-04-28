import numpy as np

answers = [
    # 51. Create a structured array representing a position (x,y) and a color (r,g,b)
    np.zeros(10, dtype=[('position', [('x', float), ('y', float)]), ('color', [('r', float), ('g', float), ('b', float)])]),

    # 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances
    np.linalg.norm(np.random.rand(100,2) - np.random.rand(100,2), axis=1),

    # 53. How to convert a float (32 bits) array into an integer (32 bits) in place?
    np.random.rand(10).astype(np.float32).astype(np.int32),

    # 54. How to read the following file? (with missing values)
    np.genfromtxt('file.txt', delimiter=",", filling_values=np.nan),  # fayl nomi file.txt deb olindi

    # 55. What is the equivalent of enumerate for NumPy arrays?
    list(np.ndenumerate(np.array([[1,2],[3,4]]))),

    # 56. Generate a generic 2D Gaussian-like array
    np.exp(-((np.linspace(-1,1,10)[:,None])**2 + (np.linspace(-1,1,10)[None,:])**2)),

    # 57. How to randomly place p elements in a 2D array?
    np.random.choice(100, 10, replace=False).reshape(2,5),

    # 58. Subtract the mean of each row of a matrix
    (lambda Z: Z - Z.mean(axis=1, keepdims=True))(np.random.rand(5, 10)),

    # 59. How to sort an array by the nth column?
    (lambda A: A[A[:,1].argsort()])(np.random.rand(5, 3)),

    # 60. How to tell if a given 2D array has null columns?
    (lambda Z: np.any(np.all(Z == 0, axis=0)))(np.random.randint(0,2,(5,5))),

    # 61. Find the nearest value from a given value in an array
    (lambda Z, val: Z.flat[np.abs(Z-val).argmin()])(np.random.rand(10), 0.5),

    # 62. Considering two arrays with shape (1,3) and (3,1), compute their sum using an iterator
    np.add.outer(np.random.rand(1,3), np.random.rand(3,1)),

    # 63. Create an array class that has a name attribute
    (lambda: type('named_array', (np.ndarray,), {"name": "my_array"}))( ),

    # 64. Add 1 to each element indexed by second vector
    (lambda Z, I: np.add.at(Z, I, 1) or Z)(np.zeros(10, int), [1,2,2,3,4,4,4]),

    # 65. Accumulate elements of X into F based on I
    (lambda X, I: np.add.at(np.zeros(5), I, X) or X)(np.arange(8), [0,1,1,2,3,3,3,4]),

    # 66. Compute number of unique colors in an image
    (lambda img: len(np.unique(img.reshape(-1,3), axis=0)))(np.random.randint(0,256,(64,64,3),dtype=np.uint8)),

    # 67. Sum over last two axis at once
    (lambda Z: Z.sum(axis=(-2,-1)))(np.random.rand(3,4,5,6)),

    # 68. Compute means of subsets of D
    (lambda D, S: [D[S==i].mean() for i in np.unique(S)])(np.random.rand(10), np.random.randint(0,3,10)),

    # 69. Get the diagonal of a dot product
    (lambda A, B: np.einsum('ij,ji->i', A, B))(np.random.rand(3,3), np.random.rand(3,3)),

    # 70. Insert 3 zeros between each value
    (lambda Z: np.reshape(np.c_[Z, np.zeros((len(Z),3))], (len(Z)*4))[:-3])(np.array([1,2,3,4,5])),

    # 71. Multiply (5,5,3) array by (5,5)
    (lambda A,B: A * B[:,:,None])(np.random.rand(5,5,3), np.random.rand(5,5)),

    # 72. Swap two rows of an array
    (lambda A: (A[[1,0,2],:] if len(A)>2 else A))(np.random.rand(3,3)),

    # 73. Find unique line segments from triangles
    (lambda triangles: np.unique(np.sort(np.concatenate([triangles[:,[0,1]], triangles[:,[1,2]], triangles[:,[2,0]]]), axis=1), axis=0))(np.random.randint(0,10,(10,3))),

    # 74. Given bincount array C, produce array A
    (lambda C: np.repeat(np.arange(len(C)), C))(np.array([0,2,1,0,3])),

    # 75. Sliding window mean
    (lambda Z, window: np.convolve(Z, np.ones(window)/window, mode='valid'))(np.random.rand(10), 3),

    # 76. Build a sliding shifted 2D array
    (lambda Z: np.lib.stride_tricks.sliding_window_view(Z, window_shape=3))(np.arange(14)),

    # 77. Negate boolean or change sign of float
    (lambda Z: np.logical_not(Z) if Z.dtype==bool else np.negative(Z))(np.array([True, False, True])),

    # 78. Compute distance from a point to lines
    (lambda P0,P1,p: np.cross(P1-P0, p-P0)/np.linalg.norm(P1-P0,axis=1))(np.random.rand(5,2), np.random.rand(5,2), np.random.rand(2)),

    # 79. Distance from multiple points to lines
    (lambda P0,P1,P: np.abs(np.cross(P1-P0, P[:,None]-P0)/np.linalg.norm(P1-P0,axis=1)))(np.random.rand(5,2), np.random.rand(5,2), np.random.rand(10,2)),

    # 80. Extract subpart centered on element with padding
    (lambda Z, shape, pos: np.pad(Z, [(s//2, s//2) for s in shape], mode='constant')[pos[0]:pos[0]+shape[0], pos[1]:pos[1]+shape[1]])(np.random.rand(10,10), (5,5), (5,5)),

    # 81. Generate [[1,2,3,4], [2,3,4,5], ..., [11,12,13,14]]
    (lambda Z: np.lib.stride_tricks.sliding_window_view(Z, window_shape=4))(np.arange(1,15)),

    # 82. Compute matrix rank
    np.linalg.matrix_rank(np.random.rand(5,5)),

    # 83. Find most frequent value
    (lambda Z: np.bincount(Z).argmax())(np.random.randint(0,10,50)),

    # 84. Extract all contiguous 3x3 blocks
    (lambda Z: np.lib.stride_tricks.sliding_window_view(Z, (3,3)))(np.random.rand(10,10)),

    # 85. Create symmetric 2D array subclass
    (lambda: type('Symmetric', (np.ndarray,), {'__getitem__': lambda self, idx: super(type(self),self).__getitem__((max(idx), min(idx)))}))(),

    # 86. Sum of p matrix products
    (lambda M, V: np.tensordot(M,V,axes=[[1],[0]]).sum(axis=0))(np.random.rand(3,4,4), np.random.rand(3,4,1)),

    # 87. Get 4x4 block-sum from 16x16 array
    (lambda Z: Z.reshape(4,4,4,4).sum(axis=(2,3)))(np.random.rand(16,16)),

    # 88. Game of Life simple step
    (lambda Z: (np.convolve(Z.ravel(), np.ones((9,)), mode='same').reshape(Z.shape)-Z) == 3)(np.random.randint(0,2,(10,10))),

    # 89. Get n largest values
    (lambda Z, n: Z[np.argsort(Z)[-n:]])(np.random.rand(10), 3),

    # 90. Cartesian product of vectors
    (lambda arrays: np.array(np.meshgrid(*arrays)).T.reshape(-1, len(arrays)))([np.array([1,2]), np.array([3,4])]),

    # 91. Create record array from regular array
    (lambda Z: Z.view([('a',Z.dtype),('b',Z.dtype)]))(np.array([[1,2],[3,4],[5,6]])),

    # 92. Cube vector in 3 ways
    (lambda Z: (Z**3, np.power(Z,3), np.multiply(Z,Z*Z)))(np.random.rand(5)),

    # 93. Find rows of A containing elements of B
    (lambda A,B: np.array([row for row in A if all(elem in row for elem in B.flatten())]))(np.random.randint(0,5,(8,3)), np.random.randint(0,5,(2,2))),

    # 94. Extract rows with unequal values
    (lambda Z: Z[~(Z[:,0]==Z[:,1]) | ~(Z[:,1]==Z[:,2])])(np.random.randint(0,5,(10,3))),

    # 95. Convert vector of ints into binary matrix
    (lambda Z: ((Z[:,None] & (1 << np.arange(8))) > 0).astype(int))(np.array([1,2,3,4])),

    # 96. Extract unique rows
    (lambda Z: np.unique(Z, axis=0))(np.random.randint(0,2,(6,3))),

    # 97. Einsum equivalents
    (lambda A,B: (np.einsum('i,i->', A, B), np.einsum('i,j->ij', A, B), np.einsum('i->', A), np.einsum('i,i->i', A, B)))(np.random.rand(5), np.random.rand(5)),

    # 98. Sample path with equidistant samples
    (lambda X,Y: np.interp(np.linspace(0,1,10), np.linspace(0,1,len(X)), X))(np.random.rand(10), np.random.rand(10)),

    # 99. Select multinomial draw rows
    (lambda X, n: X[np.all(X.astype(int) == X, axis=1) & (X.sum(axis=1) == n)])(np.random.randint(0,5,(10,5)), 10),

    # 100. Bootstrapped 95% CI for mean
    (lambda X: np.percentile([np.mean(np.random.choice(X, size=X.size, replace=True)) for _ in range(1000)], [2.5, 97.5]))(np.random.rand(100)),
]
