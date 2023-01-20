# https://pyparrot.readthedocs.io/en/latest/_modules/pyparrot/DroneVision.html
#Buffer method. Attempt to use created buffer to get frames. Issues with how the buffer works and converting to numpy array and images
#made this method difficult to use and so the callback function was used instead.
from pyparrot.Bebop import Bebop
from pyparrot.DroneVision import DroneVision
import cv2
import ffmpeg
import time
import math
import numpy
from PIL import Image

bebop = Bebop()
print("connecting")
success = bebop.connect(5)
print(success)
bebop.set_video_resolutions('rec1080_stream480')
bebop.set_picture_format('jpeg')
vision = DroneVision(bebop, is_bebop=True, buffer_size=200)
# vision.open_video()
# time.sleep(5)
# counter = 0
# while (counter < 10):
#     vision_array = numpy.array(vision.buffer[counter * 10])
#     img = Image.fromarray(vision_array,'RGB')
#     img.save("./pic" + str(counter) + ".png")
#     time.sleep(2)
#     counter+=1
print("It is done")
bebop.disconnect()