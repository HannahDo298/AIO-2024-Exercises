# -*- coding: utf-8 -*-
"""Module 02 - Vector Exercise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D9NlCFdcXsMEGfdE6oRlxOgP4ZVRciBx
"""

import numpy as np

#Compute the length of a vector

def compute_vector_length(vector):
  return np.sqrt(np.sum(vector**2))

#Compute dot product

def compute_dot_product(vector1, vector2):
  result = np.dot(vector1, vector2)
  return result

#Multiplying a vector by a matrix

def multiply_vector_by_matrix(matrix, vector):
  result = np.dot(matrix, vector)
  return result

#Multiflying matrices

def multiply_matrices(matrix1, matrix2):
  result = np.dot(matrix1, matrix2)
  return result

#Finding inverse matrix

def inverse_matrix(matrix):
  det = np.linalg.det(matrix)
  if det == 0:
    raise ValueError("Matrix is singular")
  result = (1 / det) * np.array([[matrix[1, 1], -matrix[0, 1]],
                                 [-matrix[1, 0], matrix[0, 0]]])
  return result

#Eigenvector and eigenvalue
import numpy as np

def compute_eigenvalues_eigenvectors(matrix):
    # Extract elements of the matrix
    a, b, c, d = matrix[0, 0], matrix[0, 1], matrix[1, 0], matrix[1, 1]

    # Coefficients of the characteristic polynomial
    Coeff = [1, -(a + d), a * d - b * c]

    # Find the eigenvalues
    eig = np.roots(Coeff)

    # Find the eigenvectors
    eigenvectors = []
    for i in eig:
        B = matrix - i * np.eye(2)

        # Avoid trivial solution
        perturbation = np.eye(matrix.shape[0]) * 1e-10
        B = B + perturbation

        # Create a zero vector for the right-hand side of the equation
        zero_vector = np.zeros(B.shape[0])
        zero_vector[0] = 1  # Fix the first component to avoid the trivial solution

        # Solve for the eigenvector
        v = np.linalg.solve(B, zero_vector)
        eigenvectors.append(v)

    # Find the normalized value
    normalized_eigenvectors = [v / np.linalg.norm(v) for v in eigenvectors]
    return eig, eigenvectors, normalized_eigenvectors

A = np.array([[0.9, 0.2], [0.1, 0.8]])
eig, eigenvectors, normalized_eigenvectors = compute_eigenvalues_eigenvectors(A)
print("Eigenvalues:", eig)
print("Eigenvectors:", eigenvectors)
print("Normalized_Eigenvectors:", normalized_eigenvectors)

# Cosine Similarity
def compute_cosine(v1, v2):
  cossin = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
  return cossin

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
cosine_similarity = compute_cosine(x, y)
print("Cosine Similarity:", cosine_similarity)

# Background subtraction
import numpy as np
import cv2
from google . colab . patches import cv2_imshow

# Import images and resize
bg1_image = cv2. imread ("/content/GreenBackground.png", 1)
bg1_image = cv2. resize ( bg1_image , (678 , 381) )

ob_image = cv2 . imread ("/content/Object.png", 1)
ob_image = cv2 . resize ( ob_image , (678 , 381) )

bg2_image = cv2. imread ("/content/NewBackground.jpg", 1)
bg2_image = cv2. resize ( bg2_image , (678 , 381) )

bg1_image.dtype

# Compute absolute difference
def compute_difference ( bg_img , input_img ):
  difference = cv2. absdiff ( bg_img , input_img )
  return difference

difference_single_channel = compute_difference ( bg1_image , ob_image )
cv2_imshow ( difference_single_channel )

# Compute binary mask

def compute_binary_mask ( difference_single_channel ) :
  _, difference_binary = cv2. threshold ( difference_single_channel , 0 , 255 , cv2. THRESH_BINARY )
  return difference_binary

binary_mask = compute_binary_mask ( difference_single_channel )
cv2_imshow ( binary_mask )

def replace_background ( bg1_image , bg2_image , ob_image ) :
  # Compute absolute difference
  difference_single_channel = compute_difference (bg1_image , ob_image)
  # Compute binary mask
  binary_mask = compute_binary_mask ( difference_single_channel )
  # Replace background
  output = np. where ( binary_mask ==255 , ob_image , bg2_image )
  return output

output = replace_background ( bg1_image , bg2_image , ob_image )
cv2_imshow ( output )