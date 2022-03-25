import cv2

img=cv2.imread("dribbler.jpg.jpg")
img2=cv2.imread("argentina.jpg")

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

img=cv2.resize(img, (480,480))
img2=cv2.resize(img2, (480,480))

twoimg=cv2.addWeighted(img, .9,img2, .2, 0)
#ball=img[364:412, 443:490]
#img[300:323, 360:325]=ball

cv2.imshow("image", twoimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
