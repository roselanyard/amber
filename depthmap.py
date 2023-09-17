import asyncio

import numpy
import asyncio
import sharedvars
import camera
import time
#
# local_image = numpy.zeros((depthmap_m, depthmap_n))
# async def updateDepthMap():
#     async with sharedvars.amplitudes_lock():
#         local_image = camera.get_greyscale_frame()
#



# pip3 install hilbertcurve -- in terminal
import numpy as np
from hilbertcurve.hilbertcurve import HilbertCurve

disparity_image= [[-16, -16, -16, -16, -16, -16, 155, -16],
 [ 59, 114,  -3,  14,  42, -16,  87, 127],
 [-16, 114,  47,  61,  24,  14,  23,  -8],
 [ 16,  44,  28,  41,   0,  18, -16, -16],
 [  6, -16, -16,  42,  58,  38,  31,   0],
 [-16, -16, 132, 134, 157, 196,  79,  12],
 [178,  20, -16, 368, 364,  74, 170, 196],
 [-16, 200, -16, 181, -16, 214, -16,  64]]




# normalize disparity_image
# normalized_value=
# （value−min_value） /
# （max_value−min_value）


def normalize(matrix):
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    normalized = (matrix - min_val) / (max_val - min_val)
    return normalized

normalized_image = normalize(disparity_image)
#Test
# print(normalized_image)



def image_to_hilbert(image):
    """
    Convert 2D image data to 1D using Hilbert curve.
    """
    # Ensure the image shape is 2^n x 2^n
    assert image.shape[0] == image.shape[1], "Image must be square"
    n = int(np.log2(image.shape[0]))

    # Create Hilbert Curve instance
    hilbert_curve = HilbertCurve(n, 2)

    # Convert 2D image coordinates to 1D Hilbert distances
    coordinates = [(i, j) for i in range(image.shape[0]) for j in range(image.shape[1])]
    distances = hilbert_curve.distances_from_points(coordinates)

    # Map image data to 1D using Hilbert distances
    one_d_image = np.zeros_like(image.flatten())
    for idx, dist in enumerate(distances):
        one_d_image[dist] = image[coordinates[idx][0], coordinates[idx][1]]

    return one_d_image

#Test
# one_d_data = image_to_hilbert(normalized_image)
# print("Original Image:")
# print(normalized_image)
# print("\n1D Data:")
# print(one_d_data)

def split_and_reduce(data):
    """
    Split the data into L and R, reverse R and then reduce both L and R to target_length.
    """
    half_length = len(data) // 2
    L = data[:half_length]
    R = data[half_length:]

    # Reverse R
    R = R[::-1]

    # Reduce function: Here we are using simple averaging to reduce the data.
    # More advanced reduction techniques can be implemented based on the needs.
    #def reduce_data(array, target_len):
    #    factor = len(array) // target_len
    #    return np.array([np.mean(array[i:i+factor]) for i in range(0, len(array), factor)])

    # Reduce L and R
    #L_reduced = reduce_data(L, target_length // 2)
   # R_reduced = reduce_data(R, target_length // 2)

    #return L_reduced, R_reduced
    return L, R

# Test
# Assuming target length is k*k (e.g., 16 for k=4)
# k = 4
# target_length = k * k
# L, R = split_and_reduce(one_d_data, target_length)
#
# print("L:", L)
# print("R:", R)
def update_amplitudes():
    while sharedvars.exiting is not True:
        with sharedvars.depthmap_lock:
            hilbert_curve_mapping = image_to_hilbert(sharedvars.kbyk_depthmap)
        path_L, path_R = split_and_reduce(hilbert_curve_mapping)
        with sharedvars.amplitudes_lock:
            sharedvars.amplitudes_L = path_L.tolist()
            sharedvars.amplitudes_R = path_R.tolist()
        time.sleep(0.1)