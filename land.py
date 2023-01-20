#Landing code for emergency landings if drone goes out of control or behaves oddly.

from pyparrot.Bebop import Bebop
from pyparrot.DroneVision import DroneVision
import cv2
import ffmpeg
import time


bebop = Bebop()
print("connecting")
success = bebop.connect(5)
print(success)
vision = DroneVision(bebop, is_bebop=True)
bebop.start_video_stream()
time.sleep(5)
img = vision.get_latest_valid_picture()

if(img is None):
    print("nothing happened")
else:
    print("something happened")
    filename = "test_img3.png"
    cv2.imwrite(filename,img)

print("Landing")
bebop.safe_land(5)
bebop.smart_sleep(5)

print("disconnect")
bebop.disconnect()