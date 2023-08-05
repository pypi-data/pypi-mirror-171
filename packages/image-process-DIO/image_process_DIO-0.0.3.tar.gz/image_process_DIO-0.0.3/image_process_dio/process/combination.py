import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_two_images_difference(image1, image2):
    '''
    Find the difference between two images
    First compare shapes between images
    Convert images to grayscale
    
    '''
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."
    image1_gray = rgb2gray(image1)
    image2_gray = rgb2gray(image2)
    (score, different_image) = structural_similarity(image1_gray, image2_gray, full=True)
    print("Similarity of the image: ", score)
    normalized_image_difference = (different_image-np.min(different_image))/(np.max(different_image)-np.min(different_image))
    return normalized_image_difference


def transferring_double_histogram(image1, image2):
    corresponding_image = match_histograms(image1, image2, multichannel=True)
    return corresponding_image
