import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def usagi(img, rect):
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    
    newimg = Image.open("usagi.png")
    newimg2 = newimg.copy()
    i_mos = newimg2.resize((w, h))
    
    img.paste(i_mos, (x1, y1), i_mos.split()[3])
    return img

cascade_file = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_file)

print("Choose 1 picture")
str = input()
img = cv2.imread(str)
if img is not None:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_list = cascade.detectMultiScale(img_gray, minSize=(10, 10))
    if len(face_list) == 0:
        quit()

    pil_img = Image.open(str)
    p_img = pil_img.copy()
    
    
    for (x, y, w, h) in face_list:
        p_img = usagi(p_img, (x, y, x + w, y + h))

    plt.imshow(np.asarray(p_img))
    plt.show()
    
    try:
        p_img.save("autousagi_" + str, "JPEG")
    except AttributeError:
        print("Couldn't save image {}".format("autousagi_" + str))
        
else:
    print("Nothing picture")