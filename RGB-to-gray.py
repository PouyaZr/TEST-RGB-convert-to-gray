import cv2

img = cv2.imread("Wall-E.jpg")
print("ShapeOfImage =", img.shape)
gray1 = img[:, :, 0]    # use concept to convert
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # use cvtColor to convert

cv2.imshow("my img", img)
cv2.imshow("gray1", gray1)
cv2.imshow("gray2", gray2)
cv2.imwrite("Wall-E_gray1.jpg", gray1)
cv2.imwrite("Wall-E_gray2.jpg", gray2)
cv2.waitKey()
cv2.destroyAllWindows() 