
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import datetime
import cv2


class LiveCamera:
    def __init__(self):
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
    
        # allow the camera to warmup
        time.sleep(0.1)
    
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
    
            # show the frame
            cv2.imshow("Pick image from camera by montaser", image)
            key = cv2.waitKey(1) & 0xFF
    
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)
            try:
                # if the q key was pressed, break from the loop
                if key is ord("q"):
                    print("\nThank you for using this tool ... goodbye!\n")
                    break
                elif key is ord("c"):
                    camera.capture(rawCapture, format="bgr")
                    camera.close()
                    image = rawCapture.array
                    #save image
                    filename = datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S.jpg")
                    cv2.imwrite(filename, image)
                    print("\nTake image ... Done!\n")
                    
                    LiveCamera()
                    
                    break
            except Exception as e:
                print("The exception is : " + str(e))
                
LiveCamera()