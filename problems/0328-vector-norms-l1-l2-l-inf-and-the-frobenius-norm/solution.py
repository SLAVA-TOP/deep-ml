import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    if norm_type == 'frobenius' and arr.ndim != 2:
        raise ValueError
    arr = arr.flatten()
    if norm_type == 'l1':
        rofl = abs(arr[0])
        for i in range (len(arr) - 1):
            rofl = rofl + abs(arr[i + 1])
    elif norm_type == 'l2' or norm_type == 'frobenius':
        rofl = arr[0]**2
        for i in range (len(arr) - 1):
            rofl = rofl + (arr[i + 1])**2
        rofl = (rofl)**0.5
    elif norm_type == 'linf':
        for i in range (len(arr)):
            arr[i] = abs(arr[i])
        rofl = max(arr)
    else:
        raise ValueError
    return float(rofl)
    # Your code here
    pass
