# import imp
import cv2
from cv2 import imshow
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import math

# from Backend.color_extraction import extract_colors
# from sklearn.metrics import check_scoring


red_color = sRGBColor(255, 0, 0) 
orange_color = sRGBColor(255, 142, 0) 
purple_color = sRGBColor(193, 0, 219) 

def color_section_01(color) :
    color1_lab = convert_color(color, LabColor) # Convert from RGB to Lab Color Space

    if color1_lab.lab_a > 0 :
        print("a channel of the red color " , math.sqrt(color1_lab.lab_a))
    else :
        print("a channel of the red color " , math.sqrt( (color1_lab.lab_a*-1) )*-1 )
    
    if color1_lab.lab_b < 0 :
        print("b channel of the red color " , math.sqrt( (color1_lab.lab_b*-1) )*-1 )
    else :
        print("b channel of the red color " , math.sqrt(color1_lab.lab_b))
        print("-----------------------------------------------------------")

# color_section_01(red_color)


yellow_color = sRGBColor(255, 252, 0) 
green_color = sRGBColor(12, 207, 0)
blue_color = sRGBColor(0, 0, 255) 
checking_color = sRGBColor(40, 157, 204)

def color_section_02(color) :
    color1_lab = convert_color(color, LabColor) # Convert from RGB to Lab Color Space

    if color1_lab.lab_a < 0 :
        print("a channel of the red color " , math.sqrt( (color1_lab.lab_a*-1) )*-1 )
    else :
        print("a channel of the red color " , math.sqrt(color1_lab.lab_a))

    if color1_lab.lab_b < 0 :
        print("b channel of the red color " , math.sqrt( (color1_lab.lab_b*-1) )*-1 )
    else :
        print("b channel of the red color " , math.sqrt(color1_lab.lab_b))

# color_section_02(green_color)


def color_sections(extracted_colors) :
    sRGB_versions = []
    for color in extracted_colors :
        sRGB_versions.append(sRGBColor(color[0], color[1], color[2]))

    color_1_LAB = convert_color(sRGB_versions[0], LabColor)
    color_2_LAB = convert_color(sRGB_versions[1], LabColor)

    if color_1_LAB.lab_a < 0 :
        color_1_LAB_achannel = int(round(math.sqrt(color_1_LAB.lab_a * -1), 0) * -1)
    else :
        color_1_LAB_achannel = int(round(math.sqrt(color_1_LAB.lab_a), 0))

    if color_1_LAB.lab_b < 0 :
        color_1_LAB_bchannel = int(round(math.sqrt(color_1_LAB.lab_b * -1), 0) * -1)
    else :
        color_1_LAB_bchannel = int(round(math.sqrt(color_1_LAB.lab_b), 0))


    # color sceheme 01
    if 70 <= color_1_LAB_achannel <= 80 and color_1_LAB_bchannel >= 70 : 
        print("Red !")
    if 30 <= color_1_LAB_achannel <= 69 and 0 <= color_1_LAB_bchannel <= 70 :
        print("Red shades")

    if 80 <= color_1_LAB_achannel and -80 <= color_1_LAB_bchannel <= -10 : 
        print("Purple !")
    if 40 <= color_1_LAB_achannel <= 80 and -80 <= color_1_LAB_bchannel <= -10 : 
        print("Purple shades !")
    
    if 30 <= color_1_LAB_achannel <= 70 and 40 <= color_1_LAB_bchannel : 
        print("Orange !")
    if 20 <= color_1_LAB_achannel <= 40 and 30 <= color_1_LAB_bchannel : 
        print("Orange shades !")


    # color sceheme 02
    if 60 <= color_1_LAB_bchannel <= 100 and (-40 <= color_1_LAB_achannel <= 0 or 0 <= color_1_LAB_achannel <= 40) : 
        print("Yellow !")
    if 0 <= color_1_LAB_bchannel <= 60 and (-40 <= color_1_LAB_achannel <= 0 or 0 <= color_1_LAB_achannel <= 40) : 
        print("Yellow shades !")

    if 0 <= color_1_LAB_bchannel <= 100 and -100 <= color_1_LAB_achannel <= -50 : 
        print("Green !")
    if 0 <= color_1_LAB_bchannel <= 100 and -50 <= color_1_LAB_achannel <= 0 : 
        print("Green shades !")

    if -100 <= color_1_LAB_bchannel <= -50 and 60 <= color_1_LAB_achannel <= 100 : 
        print("Blue !")
    if -50 <= color_1_LAB_bchannel <= 0 and (0 <= color_1_LAB_achannel <= 60 or -60 <= color_1_LAB_achannel <= 0) : 
        print("Blue shades !")
    if -100 <= color_1_LAB_bchannel <= -50 and (0 <= color_1_LAB_achannel <= 60 or -60 <= color_1_LAB_achannel <= 0) : 
        print("Blue shades !")
    
    print(int(round(math.sqrt(color_1_LAB.lab_l), 0)))

extracted_colors = [ (131, 188, 118), (12, 207, 0) ]
color_sections(extracted_colors) 
















def image_manipulation():
    original_image = cv2.imread('images/Yellow_Image.jpg')
    cv2.imshow("Yellow Image" ,original_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func

    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)[:,:,0]
    cv2.imshow("Processed Image" ,processed_image)
    cv2.waitKey(0) # infinite time | belongs to the upper show func


cv2.destroyAllWindows()
