import cv2
import numpy as np

SCALE = 10
WIDTH, HEIGHT = 120 * SCALE, 80 * SCALE
BACKGROUND = 0, 128 / 255.0, 0

img = np.zeros((HEIGHT, WIDTH, 3))
img[:] = BACKGROUND


def draw_lines(start, end):
    start = (start[0] * SCALE, start[1] * SCALE)
    end = (end[0] * SCALE, end[1] * SCALE)

    cv2.line(img, start, end, (1, 1, 1), 3)


def draw_cicle(centre, radius):
    radius = radius * SCALE
    centre = (centre[0] * SCALE, centre[1] * SCALE)
    cv2.circle(img, centre, radius, (1, 1, 1), 3)


def draw_rectangle(start, end):
    start = (start[0] * SCALE, start[1] * SCALE)
    end = (end[0] * SCALE, end[1] * SCALE)
    cv2.rectangle(img, start, end, BACKGROUND, cv2.FILLED)


if __name__ == "__main__":
    try:
        scale = int(input("Enter scale for soccer pitch. 1 scale = 120px*80px: "))
    except:
        print("Error: Scale must be numeric. Continuing with default SCALE = 10")
    draw_cicle(centre=(60, 40), radius=9)
    draw_cicle(centre=(108, 40), radius=10)
    draw_cicle(centre=(120, 80), radius=1)
    draw_cicle(centre=(120, 0), radius=1)

    draw_rectangle(start=(102, 18), end=(120, 62))

    draw_lines(start=(0, 0), end=(120, 0))
    draw_lines(start=(0, 80), end=(120, 80))
    draw_lines(start=(0, 0), end=(0, 80))
    draw_lines(start=(120, 0), end=(120, 80))

    draw_lines(start=(60, 0), end=(60, 80))
    draw_lines(start=(102, 18), end=(102, 62))
    draw_lines(start=(102, 18), end=(120, 18))
    draw_lines(start=(102, 62), end=(120, 62))
    draw_lines(start=(114, 30), end=(120, 30))
    draw_lines(start=(114, 50), end=(120, 50))
    draw_lines(start=(114, 30), end=(114, 50))

    # cv2.imshow("Soccer field", img)
    # cv2.waitKey(0)

    cv2.imwrite("soccer_pitch.png", 255 * img)
    print("soccer_pitch.png saved")
