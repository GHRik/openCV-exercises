# Find aruCo marker on image

## Table of contents
1. [ Description ](#repo)
2. [ How it works? ](#how)
3. [ Results ](#res)


<a name="repo"></a>
## Description
In this place you will find how to find you aruCo "marker" on picture or grabbing by camera.
Marker is a object which we want to follow or which we want to find. In the normal using
markers is a special object (for example QR code etc.) when this special object is
see by camera something will be showing.

For example if you have markers on your wiers you can read from this markers which 
wire is which.

The result from this example is below. If you want to know how binarization or 
finding countures(step by step with examples)
looks like please visit: [here](https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/README.md) if dont work: [here](https://github.com/GHRik/openCV-exercises/blob/main/money-counting/README.md)</br>
If you want to know how ot create own marker visit [here](https://github.com/GHRik/openCV-exercises/tree/aruCo-marker/find-tag).
if dont work [visit here](https://github.com/GHRik/openCV-exercises/blob/main/find-tag/README.md)

<a name="how"></a>
## How it works?
1. Load image/Capture frame from camera
2. Get know what will be your "marker"
3. Using special function detect aruCo markers
4. Insert a small point on the center image
5. Info user, he is looking on the marker with specific ID.

Okey, then step by step:

1. Load image or capture frame from camera
if you want to load image you should use:
```python
image = cv2.imread("<location_of_image>")
```
if you want to capture frame from your camera:
```python
#with this line you will select which camera you will use
#i have only one camera, so 0 
#if you want to list camera check openCV documentation
cap = cv2.VideoCapture(0)

    #If camera will be not start capture or dont exist
    #this if will be TRUE
    if not (cap.isOpened()):
        print("Could not open video device")
        exit()
    print("Camera found... Start configuration")

    #set a width and hight of captured frame.
    #This method and videoCapture from above will
    #run slow, so dont worry if you have to 
    #wait about 10-20sec to start capture frame.
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```
2. Get know what will be your marker
Aruco have a lot of markers separated on few "dictionaries". I propouse to you to go on this [marker-generator site](https://chev.me/arucogen/).
This same site is using to test marker detection in result.
```python
        
        #This part of code represent which dictonary of aruco will be
        # used and load params from this dictionary
        arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
        arucoParams = cv2.aruco.DetectorParameters_create()
        
        #If you use this function in output you will have
        #corners - all corners of detected aruco.
        #ids - all ids of detected markers.
        (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)
```

4. Insert a small point on the center image
5. Info user, he is looking on the marker with specific ID

```python
        # if any aruco marker was detected
        if len(corners) > 0:
        
            # make loop over find aruco markers id
            for i in range(len(ids)):
            
                # we have to use it , because we need to have
                # array of 4x2 not 2x4 , it is easier to understand:
                # we want to have 4point with X and Y
                # so we dont need 4x2 array.
                realCorners = corners[i].reshape((4, 2))
                
                #assign our shapes of aruco marker to realCorners.
                (topLeft, topRight, bottomRight, bottomLeft) = realCorners
                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))

                # calculating center of aruco marker
                cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                cY = int((topLeft[1] + bottomRight[1]) / 2.0)
                
                # draw small circle to select center of aruco marker
                frame = cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
                
                #put text above aruco marker with info with id was find.
                frame = cv2.putText(frame, str(ids[i]), (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (0, 255, 0), 2)
```

<a name="res"></a>
## Result
This short video is a result(if gif dont work: [video here](https://www.youtube.com/watch?v=1Mq6FuZOOcc)):
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/aruCo-marker/aruCo-marker/images/aruco-markers.gif" width="50%" height="50%" alt="marker.gif" />
</p>

This code is working when is a more than 1 marker on frame:</br>
<p align="center">
    Image:
   <img src="https://github.com/GHRik/openCV-exercises/blob/aruCo-marker/aruCo-marker/images/arucoMarker.jpg" width="75%" height="50%" alt="marker.gif" />
</p>
<p align="center">
   Result:
   <img src="https://github.com/GHRik/openCV-exercises/blob/aruCo-marker/aruCo-marker/images/result.jpg" width="75%" height="50%" alt="marker.gif" />
</p>
