import cv2 as cv
import numpy as np

CAM_ID = 0


class VideoCamera(object):
    def __init__(self) -> None:
        self.video = cv.VideoCapture(CAM_ID)

    def __del__(self) -> None:
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if success:
            try:
                ret, buffer = cv.imencode(".jpg", cv.flip(frame, 1))
                if ret:
                    frame = buffer.tobytes()
                return frame
            except Exception as e:
                pass
