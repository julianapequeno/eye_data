
import numpy as np
from scipy.ndimage import gaussian_filter

def generate_gaussian(size_x, size_y, list_array_point, frame_nr, point_lifetime, sd_guass):

    sd_guass = sd_guass / 4

    array_image = np.zeros((size_x, size_y))

    

    for i, array_point in enumerate(list_array_point):

        x = int(array_point[0])

        y = int(array_point[1])


        # Check if the point is inside the image and add it to the heatmap

        if 0 <= y and y < array_image.shape[0] and 0 <= x and x < array_image.shape[1]:

            array_image[y, x] += 1

 

    array_image = gaussian_filter(array_image, sd_guass, mode="constant", cval=0)

    array_image *= 125 

    array_image = np.clip(array_image, 0, 1)

 

    return array_image
