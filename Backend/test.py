import cv2
from cv2 import imshow
from colormath.color_objects import AdobeRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000


# Red color
red_color = AdobeRGBColor(225, 0, 0, is_upscaled=False)

# Maroon color
blue_color = AdobeRGBColor(0, 0, 225, is_upscaled=False)

# Convert from RGB to Lab Color Space
color1_lab = convert_color(red_color, LabColor)
color2_lab = convert_color(blue_color, LabColor)

delta_e = delta_e_cie2000(color1_lab, color2_lab);
print(delta_e)

def image_manipulation():
    original_image = cv2.imread('images/Yellow_Image.jpg')
    cv2.imshow("Yellow Image" ,original_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func

    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)[:,:,0]
    cv2.imshow("Processed Image" ,processed_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func


cv2.destroyAllWindows()
