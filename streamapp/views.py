from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import VideoCamera


# Create your views here.
def index(response):
    return render(response, "streamapp/index.html")


def user(response):
    return render(response, "streamapp/user.html")


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


def video_feed(response):
    return StreamingHttpResponse(
        gen(VideoCamera()), content_type="multipart/x-mixed-replace; boundary=frame"
    )
