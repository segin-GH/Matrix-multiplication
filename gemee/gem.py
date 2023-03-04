#! usr/bin/env python3
import numpy as np

print("Hello World")

N = 4028

if __name__ == "__main__":
    # N^2
    A = np.random.randn(N, N).astype(np.float32)
    # N^2
    B = np.random.randn(N, N).astype(np.float32)
    
    # N^2 output cells with 2N compute each
    # flops print(N*N*2*N)
    
    print(N*N*2*N)
    C = A @ B
    print(C)
