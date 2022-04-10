# import imp
import cv2
from cv2 import imshow
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import math


red_color = sRGBColor(255, 0, 0) # red color -> a channel 80
orange_color = sRGBColor(255, 142, 225) # orange color -> a channel 67
purple_color = sRGBColor(193, 142, 219) # purple color -> a channel 53

# Convert from RGB to Lab Color Space
color1_lab = convert_color(purple_color, LabColor)
# color2_lab = convert_color(pink_color, LabColor)

if color1_lab.lab_a > 0 :
    print("-----------------------------------------------------------")
    print("a channel of the red color " , math.sqrt(color1_lab.lab_a))
    # print("a channel of the pink color" , color2_lab.lab_a)
    print("-----------------------------------------------------------")

# delta_e = delta_e_cie2000(color1_lab, color2_lab);
# print(delta_e)

def image_manipulation():
    original_image = cv2.imread('images/Yellow_Image.jpg')
    cv2.imshow("Yellow Image" ,original_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func

    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)[:,:,0]
    cv2.imshow("Processed Image" ,processed_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func


cv2.destroyAllWindows()
