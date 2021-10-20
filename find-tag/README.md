# Counting money from image

## Table of contents
1. [ Description ](#repo)
2. [ How it works? ](#how)
3. [ Results ](#res)

<a name="repo"></a>
## Description
In this place you will find how to find you "marker" on picture or grabbing by camera.
Marker is a object which we want to follow or which we want to find. In the normal using
markers is a special object (for example QR code etc.) when this special object is
see by camera something will be showing.

For example if you have markers on your wiers you can read from this markers which 
wire is which.

The result from this example is below. If you want to know how binarization or 
finding countures(step by step with examples)
looks like please visit: [here](https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/README.md) if dont work: [here](https://github.com/GHRik/openCV-exercises/blob/main/money-counting/README.md)

<a name="how"></a>
## How it works?
1. Load image/Capture frame from camera
2. Get know what will be your "marker"
3. Get binary image from loaded image or frame
4. Get contures of probably size your marker
5. Using theory of "moment image" calculate center of contures
6. Insert a small point on the center image
7. Info user, he is looking on center of image

Okey then step by step:

1. Load image or capture frame from camera
This step is very easy if you want to load image you should use:
```python
image = cv2.imread("<location_of_image>")
```
but if you want to capture frame from your camera it will be much complicated
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
Get up and look around. Grab a object with grab a large item of bright solid color.
It could be cup, bottle, scarf, board, bag, screw cap etc. but 
remember a solid bright color. 

3. Get binary image from loaded image or frame
If you have your marker look on it. What color there is?
If you have color , you have to make a binary image/frame from
this color you have. You have to make your color zero and all the others - one.
To better grab color use HSV color pallet.
```python
	#convert RGB to HSV pallete to better grab solid color.
	img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#The way is create 4masks
	#2group (lower - upper)
	#My mrker was red and in HSV pallete red is from
	# 0-20 and 160-180 , but "red" color can be changed
	#due to lighting, shadows, etc. 
	#So you should check your color with HSV pallete and
	#Make a small changes to have better binary image/frame
        lower = np.array([0, 100, 20])
        upper = np.array([20, 255, 255])
        lower2 = np.array([160, 100, 20])
        upper2= np.array([180, 255, 255])
	
	#Using inRange function you create binary image/frame
	#All from lower to upper will be a 255 and another will be 0
	#The same will be in binary2
        binary1 = cv2.inRange(img_hsv, lower, upper)
        binary2 = cv2.inRange(img_hsv, lower2, upper2)
	
	#Now to complete create binary we should add two result
	#from our two masks
        binary = binary1+binary2

```
4. Get contures of probably size your marker
Now if oyu have binary image/frame you should easy to grep contures,
but remember if you wrong pick your mask you will have a lot of another
object in binary image/frame.

```python
contures, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
```

5. Using theory of "moment image" calculate center of contures
To locate a center of our contures we have to using [moment image theory](https://en.wikipedia.org/wiki/Image_moment).
The best thing is a opencv make a moment calculus for us ;).
```python
		M = cv2.moments(contures[i])
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
```
where "c" is "center"

6. Insert a small point on the center image
If we have a X and Y of center is easy to point a center on our image:
```python
circle =  cv2.circle(frame.copy(), (cX, cY), 1, (255, 255, 255), 20)
```
7. Info user, he is looking on center of image
The last thing is to create text info for user he is looking on center of our marker.
But dont forget to create our contures of object, because only with contures line
a text "center" mean something
```python
#create "center" text
withCenter = cv2.putText(circle, "center", (cX - 20, cY - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
#create a conture line
frameWithContures = cv2.drawContours(image=withCenter, contours=realContures, contourIdx=-1, color=(0, 255, 0), thickness=10, lineType=cv2.LINE_AA)
```

<a name="res"></a>
## Result
This short video is a result(if gif dont work: [video here](https://www.youtube.com/watch?v=wGfBVxBY7yA)):
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/find-tag/find-tag/images/openCv-marker.gif" width="50%" height="50%" alt="marker.gif" />
</p>

