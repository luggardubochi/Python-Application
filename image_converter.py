import cv2

#Now the next thing to do is to read the image:
image = cv2.imread("dog.jpg")
cv2.imshow("Dog", image)
cv2.waitKey(0)

#Now after reading the image, we will create a new image by converting the original image to greyscale:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("New Dog", gray_image)
cv2.waitKey(0)

#Now the next step is to invert the new grayscale image:
inverted_image = 255 - gray_image
cv2.imshow("Inverted", inverted_image)
cv2.waitKey()

#Now the next step in the process is to blur the image by using the Gaussian Function in OpenCV:
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

#Then the final step is to invert the blurred image, then we can easily convert the image into a pencil sketch:
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)