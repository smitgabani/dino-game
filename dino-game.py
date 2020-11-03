import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # rectangle for birds
    for i in range(315, 450):
        for j in range(410, 538):
            if data[i, j] < 100:
                hit("down")
                return

    # rectangles for cactus
    for i in range(315, 450):
        for j in range(538, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 5 seconds")
    time.sleep(4)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        
        '''
        # print(asarray(image))
        
        # Draw the rectangle for birds
        for i in range(315, 450):
            for j in range(410, 538):
                data[i, j] = 171
        
        # Draw the rectangle for cactus
        for i in range(315, 450):
            for j in range(538, 650):
                data[i, j] = 0
        
        image.show()
        break
        '''
