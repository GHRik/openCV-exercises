# Counting money from image

## Table of contents
1. [ Description ](#repo)
2. [ How it works? ](#how)
3. [ Examples photo ](#img)
4. [ Results ](#res)

<a name="repo"></a>
## Description
In this place you will find how to count object on the images. The most easier example is count coins on the image.

<a name="how"></a>
## How it works?
1. Load image
2. Blur image
3. Change this image to grey scale
4. Image binarization
5. Morphological opening
6. Edge filtering
7. Count edge
8. Print how much is object on image

Step by step:
1. Load image - you must load image to count object on this image.
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/image_example.png" width="50%" height="50%" alt="money2.jpg" />
</p>
2. Blur image - we should have uniform coins, it means coins should have similar color in center of the money and on the edge.
To get know why you need a similary color you must go throught to point 4.
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/blured.png" width="50%" height="50%" alt="blured.jpg" />
</p>
3. Convert to grey scale, because it easier convert grey scale to binary than RGB 
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/toGrey.png" width="50%" height="50%" alt="grey.jpg" />
</p>
4. Binarization image - it is needed to properly find contures. It is very easy to find contures in binary. There are a lot of algorythm to binarization image. All of this algorythm is good for specific case. This step separate coins from the background to cois which you want to count.The best method i think is set a very high binarization threshold and then try to decrease it. When threshold is very big we can easy separate background from our object(assuming that the background is single-color and unchanging).
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/binary.png" width="50%" height="50%" alt="binarization.jpg" />
</p>
5. Morphological opening - sometimes is situation when after image bluring or on the orginal image some coins is sticks each other. With sticking is not possible to properly select and count contures. We have to make a small distance bettwen coins. So in this case we use opening. As you can see with opening is a small problem: if you opening too much times one object can disapera. 
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/opening.png" width="50%" height="50%" alt="opening.jpg" />
</p>
6. Edge filtering - Same problem as binarization algorythm. There are a lot of algorythm and it is very depends which one you should use to specific case.</br>
7. If you have a selected contures it is easy to count it</br>
8. So the printing only left.

<a name="img"></a>
## Examples money which we will count
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/money1.jpg" width="33%" height="33%" alt="money1.jpg" />
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/money2.jpg" width="33%" height="33%" alt="money2.jpg" />
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/money3.jpg" width="33%" height="33%" alt="money3.jpg" />
</p>

<a name="res"></a>
## Results:
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/result1.jpg" alt="result1.jpg" />
</p>
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/result2.jpg" alt="result2.jpg" />
</p>
<p align="center"> 
  <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/result3.jpg" alt="result3.jpg" />
</p>
