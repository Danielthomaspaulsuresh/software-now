
import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils
import pytesseract

image = cv2.imread('cdu_logo.jpg')

if image is None:
    print("error: image not found,")

else:
    cv2.imshow("image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread('cdu_logo.jpg')

if image is None:
    print("error: Image not found.")

else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.imshow(image_rgb)
plt.show()


image = cv2.imread('cdu_logo.jpg')

if image is None:
    print("error: imgae not found,")

else:
    height, width = image.shape[0:2]
    print("height: ", height)
    print("width:",width)



# extracting the region of interest

image = cv2.imread('cdu_logo.jpg')

if image is None:
    print("error:image not foundd")

else:
    x1, y1 = 25, 40# top-left
    x2, y2 = 20, 300 #bottom-right


    extract_logo = image[y1:y2,  x1:x2]
    cv2.imshow('logo', extract_logo)

    cv2.waitKey(0)
""""
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

dest_xor = cv2.bitwise_xor(image1,image2, mask = None)

image1_rgb = cv2.cvtcolor(image1, cv2.COLOR_BGR2RGB)
image2_rgb = cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
dest_xor_rgb = cv2.cvtColor(dest_xor,cv2.COLOR_BGR2RGB)

plt.figure(figsize = (15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image1_rgb)
plt.title('image 1')

plt.subplot(1, 3, 2)
plt.imshow(image2_rgb)
plt.title("image2")

plt.subplot(1, 3, 3)
plt.imshow(dest_xor_rgb)
plt.title('bitwise XOR Result')

plt.tight_layout()
plt.show()
"""