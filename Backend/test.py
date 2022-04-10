# import imp
import cv2
from cv2 import imshow
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import math
# from sklearn.metrics import check_scoring


red_color = sRGBColor(255, 0, 0) 
orange_color = sRGBColor(255, 142, 0) 
purple_color = sRGBColor(193, 0, 219) 

def color_section_01(color) :
    color1_lab = convert_color(color, LabColor) # Convert from RGB to Lab Color Space

    if color1_lab.lab_a > 0 :
        print("-----------------------------------------------------------")
        print("a channel of the red color " , math.sqrt(color1_lab.lab_a))
        if color1_lab.lab_b < 0 :
            print("b channel of the red color " , math.sqrt( (color1_lab.lab_b*-1) )*-1 )
        else :
            print("b channel of the red color " , math.sqrt(color1_lab.lab_b))
            print("-----------------------------------------------------------")

# color_section_01(red_color)


yellow_color = sRGBColor(255, 252, 0) 
green_color = sRGBColor(12, 207, 0)
blue_color = sRGBColor(0, 0, 255) 
checking_color = sRGBColor(195, 243, 192)

def color_section_02(color) :
    color1_lab = convert_color(color, LabColor) # Convert from RGB to Lab Color Space

    if color1_lab.lab_a < 0 :
        print("-----------------------------------------------------------")
        print("a channel of the red color " , math.sqrt( (color1_lab.lab_a*-1) )*-1 )
    else :
        print("a channel of the red color " , math.sqrt(color1_lab.lab_a))

    if color1_lab.lab_b < 0 :
        print("b channel of the red color " , math.sqrt( (color1_lab.lab_b*-1) )*-1 )
    else :
        print("b channel of the red color " , math.sqrt(color1_lab.lab_b))
        print("-----------------------------------------------------------")

color_section_02(checking_color)



















def image_manipulation():
    original_image = cv2.imread('images/Yellow_Image.jpg')
    cv2.imshow("Yellow Image" ,original_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func

    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)[:,:,0]
    cv2.imshow("Processed Image" ,processed_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func


cv2.destroyAllWindows()
