import cv2
from cv2 import imshow
from colormath.color_objects import AdobeRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


red_color = AdobeRGBColor(225, 0, 0) # red color

lightblue_color = AdobeRGBColor(35, 195, 225) # light-blue color
pink_color = AdobeRGBColor(240, 35, 255) # pink color

# Convert from RGB to Lab Color Space
color1_lab = convert_color(red_color, LabColor)
color2_lab = convert_color(pink_color, LabColor)

print("-----------------------------------------------------------")
print("a channel of the red color " , color1_lab)
print("a channel of the pink color" , color2_lab.lab_a)
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
