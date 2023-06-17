import numpy as np
import cv2
import pyautogui
import time
import subprocess

#subprocess.call("D:/screenCapture/upload.py", shell=True)
#import upload.py

# take screenshot using pyautogui
#exec(open("D:/Project/Python Scripts/screenCapture/upload.py").read())
def screen():
    image = pyautogui.screenshot()
    
    # since the pyautogui takes as a 
    # PIL(pillow) and in RGB we need to 
    # convert it to numpy array and BGR 
    # so we can write it to the disk
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    
    # writing it to the disk using opencv
    cv2.imwrite("C:Users\\m.surya.prasad.reddi\\screenCapture\\screenCapture\\New\\"+str(time.time())+".png", image)

while(1):
    screen()
    #upload.main()
    time.sleep(2)

    #bkjb