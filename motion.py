from pyparrot.Bebop import Bebop
from pyparrot.DroneVision import DroneVision
import cv2
import ffmpeg
import time
import math


def followLawnmowerPath(height, width, depth, scanDistance, pathWidth, bebop):
    currentHeight = pathWidth
    print("Scanning Face 1")
    currentHeight = oneFace(height, width, pathWidth, currentHeight, bebop)
    print("Finished Scanning Face 1 - Transitioning Faces")
    currentHeight = transitionFaces(width, scanDistance, pathWidth, currentHeight, bebop)
    print("Scanning Face 2")
    currentHeight = oneFace(height, depth, pathWidth, currentHeight, bebop)
    print("Finished Scanning Face 2 - Transitioning Faces")
    currentHeight = transitionFaces(depth, scanDistance, pathWidth, currentHeight, bebop)
    print("Scanning Face 3")
    currentHeight = oneFace(height, width, pathWidth, currentHeight, bebop)
    print("Finished Scanning Face 3 - Transitioning Faces")
    currentHeight = transitionFaces(width, scanDistance, pathWidth, currentHeight, bebop)
    print("Scanning Face 4")
    currentHeight = oneFace(height, depth, pathWidth, currentHeight, bebop)
    print("Finished Scanning Face 4 - Transitioning Faces")
    currentHeight = transitionFaces(depth, scanDistance, pathWidth, currentHeight, bebop)
    print("Finished Scanning")


def transitionFaces(width, scanDistance, pathWidth, currentHeight, bebop):
    move(width - pathWidth + scanDistance, 'right', bebop)
    move(pathWidth + scanDistance, 'forward', bebop)
    rotate(90, 'counterclockwise', bebop)
    move(currentHeight - pathWidth, 'down', bebop)
    return pathWidth


def oneFace(height, width, pathWidth, currentHeight, bebop):
    while currentHeight < height - pathWidth:
        oneScan(width, pathWidth, bebop)
        currentHeight += 4*pathWidth
    return currentHeight


def oneScan(width, pathWidth, bebop):
    move(width-2*pathWidth, 'right', bebop)
    move(2*pathWidth, 'up', bebop)
    move(width-2*pathWidth, 'left', bebop)
    move(2*pathWidth, 'up', bebop)


def move(dist, direction, bebop):

    # Need to Tune This
    scalingFactorForwardBackward = 1
    scalingFactorLeftRight = 1
    scalingFactorUpDown = 1

    if direction == 'forward':
        print("Going Forward for " + str(dist) + " meters")
        bebop.move_relative(dist, 0, 0, 0)
        bebop.smart_sleep(1)
    elif direction == 'backward':
        print("Going Backward for " + str(dist) + " meters")
        bebop.move_relative(-dist, 0, 0, 0)
        bebop.smart_sleep(1)
    elif direction == 'left':
        print("Going Left for " + str(dist) + " meters")
        bebop.move_relative(0, -dist, 0, 0)
        bebop.smart_sleep(1)
    elif direction == 'right':
        print("Going Right for " + str(dist) + " meters")
        bebop.move_relative(0, dist, 0, 0)
        bebop.smart_sleep(1)
    elif direction == 'down':
        print("Going Down for " + str(dist) + " meters")
        bebop.move_relative(0, 0, dist, 0)
        bebop.smart_sleep(1)
    else:
        print("Going Up for " + str(dist) + " meters")
        bebop.move_relative(0, 0, -dist, 0)
        bebop.smart_sleep(1)


def rotate(degrees, direction, bebop):

    if direction == 'counterclockwise':
        print("Turning counterclockwise by " + str(degrees) + " degrees")
        bebop.move_relative(0, 0, 0, math.radians(-degrees))
        bebop.smart_sleep(2)
    else:
        print("Turning clockwise by " + str(degrees) + " degrees")
        bebop.move_relative(0, 0, 0, math.radians(degrees))
        bebop.smart_sleep(2)


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

print("taking off!")
bebop.safe_takeoff(5)

print("Take off successful, waiting 5 seconds")
bebop.smart_sleep(5)

# Set Values According to Size of Building
height = 1.219
width = 0.6096
depth = 0.4572
scanDistance = 0.3
pathWidth = 0.1

print("Begin Scanning Along Lawnmower Path")
followLawnmowerPath(height, width, depth, scanDistance, pathWidth, bebop)
print("Finished Scanning Along Lawnmower Path")

# Land, Ending Flight
print("landing")
bebop.safe_land(5)
bebop.smart_sleep(5)

print("disconnect")
bebop.disconnect()