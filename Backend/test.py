import cv2
from cv2 import imshow

original_image = cv2.imread('images/Yellow_Image.jpg')
cv2.imshow("Yellow Image" ,original_image)
cv2.waitKey(0) # infinite time | belongs to the upper show func

processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Processed Image" ,processed_image)
cv2.waitKey(0) # infinite time | belongs to the upper show func


cv2.destroyAllWindows()
