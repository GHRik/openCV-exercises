import cv2

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

    while True:
        ret, frame = cap.read()
        arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
        arucoParams = cv2.aruco.DetectorParameters_create()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
        if len(corners) > 0:
            for i in range(len(ids)):
                realCorners = corners[i].reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = realCorners
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))

                frame = cv2.line(frame, topLeft, topRight, (0, 255, 0), 10)
                frame = cv2.line(frame, topRight, bottomRight, (0, 255, 0), 10)
                frame = cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 10)
                frame = cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 10)

                cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                frame = cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

                frame = cv2.putText(frame, str(ids[i]), (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 255, 0), 2)

        cv2.imshow('preview', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
