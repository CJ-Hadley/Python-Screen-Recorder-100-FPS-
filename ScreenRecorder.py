import time
import cv2
import mss
import numpy


with mss.mss() as capture:
  area = {"top": 40, "left": 0, "width": 800, "height": 640}
  while "Screen capturing":
    last_time = time.time()
    img = numpy.array(capture.grab(area))
    task = '{}'.format(area)
    cv2.imshow("ScreenRecorder: area being recorded :: [{}]".format(task), img)
  
    print("fps: {}".format(1 / (time.time() - last_time)))
    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
