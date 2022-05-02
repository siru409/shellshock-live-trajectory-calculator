import math
from pynput.mouse import Listener
import pyautogui


w, h = pyautogui.size()
print(str(h)+"p")
g = (370/1080) * h
i = 0
v_pr = (9.71/1080) * h
coordinates = [[0, 0], [0, 0], [0, 0]]
offset = [0, 0]
enable = False


def calc():
    global i
    global g
    global enable
    i = 0
    faktoren = []
    for num in range(1, 3):
        faktoren.append([(coordinates[num][0]) ** 2, coordinates[num][0], coordinates[num][1]])
    try:
        scal = -faktoren[1][0]/faktoren[0][0]
        b = (faktoren[1][2]+scal*faktoren[0][2])/(faktoren[1][1]+scal*faktoren[0][1])
    except Exception as e:
        print("select three different coordinates!", e)
        return
    a = (faktoren[0][2]-faktoren[0][1]*b)/faktoren[0][0]
    angle = math.atan(b)
    try:
        velocity = math.sqrt((0.5*g)/((math.cos(angle)**2)*a))
    except:
        print('impossible shot!')
        return
    angle = angle*(180/math.pi)
    if coordinates[2][0] > coordinates[0][0]:
        angle = -angle
    print(f'velocity: {round(velocity/v_pr, 1)}% | angle: {round(angle, 1)}°')
    enable = False


def on_click(x, y, button, pressed):
    global i
    global coordinates
    global offset
    global enable
    if pressed and str(button) == "Button.right":
        print("input:")
        enable = True
    if pressed and str(button) == "Button.left":
        if i < 3 and enable:
            if i == 0:
                offset[0] = x
                offset[1] = y
            coordinates[i][0] = x
            coordinates[i][1] = y
            coordinates[i][0] -= offset[0]
            coordinates[i][1] -= offset[1]
            print(f"Point {i}")
            i += 1
            if i == 3:
                calc()


if __name__ == '__main__':
    with Listener(on_click=on_click) as listener:
        listener.join()
