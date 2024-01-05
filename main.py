import numpy as np
import cv2 as cv
from datetime import datetime

drawing = False  # true if mouse is pressed
mode = 'rec'  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1
r, g, b = 0, 0, 0
rad = 0


def nothing(x):
    pass


# mouse callback function
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == 'rec':
                cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)

            if mode == 'line':
                cv.line(img, (ix, iy), (x, y), (b, g, r), 1)

    elif event == cv.EVENT_LBUTTONDBLCLK:
        if mode == 'cir':
            cv.circle(img, (x, y), rad, (b, g, r), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


# Create a black image, a window and bind the function to window
img = np.full((1024, 1024, 3), 255, np.uint8)

cv.namedWindow('My Paint')
cv.setMouseCallback('My Paint', draw)

cv.createTrackbar('R', 'My Paint', 0, 255, nothing)
cv.createTrackbar('G', 'My Paint', 0, 255, nothing)
cv.createTrackbar('B', 'My Paint', 0, 255, nothing)

cv.createTrackbar('Radius', 'My Paint', 0, 100, nothing)


while True:
    cv.imshow('My Paint', img)
    k = cv.waitKey(1) & 0xFF

    if k == ord('c'):
        mode = 'cir'
    if k == ord('r'):
        mode = 'rec'
    if k == ord('l'):
        mode = 'line'

    if k == ord('s'):
        name = datetime.now().strftime('%m-%d-%Y, %H-%M-%S')
        file_path = f"output/img-{name}.png"
        cv.imwrite(
            file_path, img)
        print("saved")

    elif k == 27:
        break

    r = cv.getTrackbarPos('R', 'My Paint')
    g = cv.getTrackbarPos('G', 'My Paint')
    b = cv.getTrackbarPos('B', 'My Paint')

    rad = cv.getTrackbarPos('Radius', 'My Paint')

    cv.rectangle(img, (0, 0), (60, 30), (b, g, r), -1)


cv.destroyAllWindows()
