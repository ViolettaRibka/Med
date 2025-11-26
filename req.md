import cv2

image_np = cv2.imread('images/otter/jpg')

# ВНИМАНИЕ! В OpenCV первым аргументом идет ВЫСОТА!
# sliced_region = image_np[:, 50:150]

# image_np[:, 50:150] = (255,0,0)

# cv2.imshow('Sliced Image', sliced_region)
cv2.imshow('Sliced Image', image_np)
cv2.waitKey(0)
cv2.destroyAllWindows()