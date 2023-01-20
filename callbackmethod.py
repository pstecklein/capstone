# https://pyparrot.readthedocs.io/en/latest/_modules/pyparrot/DroneVision.html
#Currently the main image taking method. Other image taking related files are deprecated.
from pyparrot.Bebop import Bebop
from pyparrot.DroneVision import DroneVision
import cv2
import ffmpeg
import time
import math
import numpy

class Callbacker:
    def __init__(self,vision):
        self.counter = 0
        self.vision = vision
    def callback(self,args):
        print("this is running")
        img = self.vision.get_latest_valid_picture()
        if img is not None:
            filename = "./zpic" + str(self.counter) + ".png"
            cv2.imwrite(filename,img)
            self.counter+=1

bebop = Bebop()
print("connecting")
success = bebop.connect(5)
print(success)
bebop.set_video_resolutions('rec720_stream720') #Possible changes here for quality
vision = DroneVision(bebop, is_bebop=True)
callbacker = Callbacker(vision)
vision.set_user_callback_function(callbacker.callback, user_callback_args=None)
vidsuccess = vision.open_video()
if vidsuccess:
    bebop.smart_sleep(480)
    vision.close_video()
else:
    print("error")
print("It is done")
bebop.disconnect()

