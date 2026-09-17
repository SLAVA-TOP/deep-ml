import numpy as np

def calculate_dot_product(vec1, vec2):
	rofl = 0
	for i in range(len(vec1)):
		rofl = (vec1[i] * vec2[i]) + rofl
	return rofl
	
	# Your code here
	pass