#Test code to be able to take a picture and save it. Method only returned the last picture repeatedly due to how buffer works.
#As a result last_valid_picture in this context was dropped.
from pyparrot.Bebop import Bebop
from pyparrot.DroneVision import DroneVision
import cv2
import ffmpeg
import time
import math

bebop = Bebop()
print("connecting")
success = bebop.connect(5)
print(success)
bebop.set_video_resolutions('rec1080_stream480')
vision = DroneVision(bebop, is_bebop=True)
bebop.start_video_stream()
vision.open_video()
time.sleep(5)
# vision.open_video()
# counter = 0
# while counter < 30:
#     img = vision.get_latest_valid_picture()
#     if(img is None):
#         print("nothing happened")
#     else:
#         print("something happened")
#         filename = "test_img" + str(counter) + ".png"
#         cv2.imwrite(filename,img)
#     counter+=1
#     time.sleep(1)

#C:\Users\CPS\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyparrot\utils
bebop.disconnect()