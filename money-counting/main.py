import cv2
import numpy as np

if __name__ == '__main__':
    image = cv2.imread("monety2.jpg")
    image_blur = cv2.GaussianBlur(image, (9, 9), 1)

    image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)
    image_res, image_thresh = cv2.threshold(image_blur_gray, 250, 255, cv2.THRESH_BINARY_INV)
    mask = np.ones((3, 3), np.uint8)

    amountOfMoney = 0
    MAX_ITER = 50
    for iteration in range(MAX_ITER):
        actualAmountOfMoney = 0
        opening = cv2.morphologyEx(image_thresh, cv2.MORPH_OPEN, mask, iterations=iteration)
        contures, hierarchy = cv2.findContours(opening, 1, 2)
        bigSize = 10000
        for i in range(len(contures)):
            if cv2.contourArea(contures[i]) > bigSize:
                actualAmountOfMoney = actualAmountOfMoney + 1

        if amountOfMoney <= actualAmountOfMoney:
            amountOfMoney = actualAmountOfMoney
        else:
            break
    print("Total Money Count = {}".format(amountOfMoney))