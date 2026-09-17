import numpy as np

def cosine_similarity(v1, v2):
    rofl1 = 0
    for i in range(len(v1)):
        rofl1 = v1[i] * v2[i] + rofl1
        
    rofl2 = v1[0]**2
    for i in range(len(v1) - 1):
        rofl2 = rofl2 + (v1[i + 1])**2
    rofl2 = (rofl2)**0.5
    
    rofl3 = v2[0]**2
    for i in range(len(v2) - 1):
        rofl3 = rofl3 + (v2[i + 1])**2
    rofl3 = (rofl3)**0.5
    
    rofl = rofl1 / (rofl2 * rofl3)
    return float(rofl)
