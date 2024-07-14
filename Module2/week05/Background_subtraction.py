import numpy as np
import cv2

bg1_image = cv2.imread(
    "/media/tan/F/AIO2024_hw/AIO2024_hw/Module2/week05/Image_data/GreenBackground.png")
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread(
    '/media/tan/F/AIO2024_hw/AIO2024_hw/Module2/week05/Image_data/Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread(
    '/media/tan/F/AIO2024_hw/AIO2024_hw/Module2/week05/Image_data/NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    input_gray = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

    difference = cv2.absdiff(bg_gray, input_gray)
    return difference


def compute_binary_mask(difference_single_channel):

    _, binary_mask = cv2.threshold(
        difference_single_channel, 10, 255, cv2.THRESH_BINARY)

    return binary_mask


def replace_background(bg1_image, bg2_image, ob_image):

    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)

    binary_mask_3ch = cv2.merge([binary_mask, binary_mask, binary_mask])

    output = np.where(binary_mask_3ch == 255, ob_image, bg2_image)

    return output


difference_single_channel = compute_difference(bg1_image, ob_image)
cv2.imshow("Single channel", difference_single_channel)

binary_mask = compute_binary_mask(difference_single_channel)
cv2.imshow("Binary mask", binary_mask)

output_image = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow("Output image", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
