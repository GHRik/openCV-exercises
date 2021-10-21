import cv2
import numpy as np

if __name__ == '__main__':

    cap = cv2.VideoCapture(0)
    if not (cap.isOpened()):
        print("Could not open video device")
        exit()
    print("Camera found... Start configuration")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    print("Configuration done...")
    cv2.startWindowThread()
    cv2.namedWindow("preview")

    while (True):
        ret, frame = cap.read()
        img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 100, 20])
        upper = np.array([20, 255, 255])
        lower2 = np.array([160, 100, 20])
        upper2= np.array([180, 255, 255])

        binary1 = cv2.inRange(img_hsv, lower, upper)
        binary2 = cv2.inRange(img_hsv, lower2, upper2)

        binary = binary1+binary2

        contures, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        realContures = []
        for i in range(len(contures)):
            if cv2.contourArea(contures[i]) > 5000:
                realContures.append(contures[i])
        if len(realContures) > 0:
            for i in range(len(realContures)):
                M = cv2.moments(realContures[i])
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                circle =  cv2.circle(frame.copy(), (cX, cY), 1, (255, 255, 255), 20)
                withCenter = cv2.putText(circle, "center", (cX - 20, cY - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            frameWithContures = cv2.drawContours(image=withCenter, contours=realContures, contourIdx=-1, color=(0, 255, 0), thickness=10, lineType=cv2.LINE_AA)
        else:
            frameWithContures = frame
        cv2.imshow("preview",frameWithContures)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break