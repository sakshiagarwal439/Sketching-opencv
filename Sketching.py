import cv2

#Function to dodge and burn the image
def dodgeV2(x, y):
    return cv2.divide(x, 255-y, scale=256)


img_bgr = cv2.imread('photo.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img_bgr)

#Invert the image to make brighter parts darker and darker parts brighter
img_invert = cv2.bitwise_not(img_gray)

#Reducing the noise in the image
img_smooth = cv2.GaussianBlur(img_invert, (21, 21), sigmaX = 0, sigmaY = 0)

final_img = dodgeV2(img_gray, img_smooth)
cv2.imshow("Final Image", final_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
