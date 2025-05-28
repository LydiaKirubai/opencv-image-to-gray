import cv2

img = cv2.imread("yourpath/picture.jpg")
 
# Convert image to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display Image
cv2.imshow("Image",gray)

# Close only when user closes the window
cv2.waitKey(0)
cv2.destroyAllWindows()