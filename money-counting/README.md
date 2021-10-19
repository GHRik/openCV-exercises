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

Okey so now step to step:
1. Load image - it is easy , we must load image to count object on this image, nothing more to say :)
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/example/image_example.png" width="50%" height="50%" alt="money2.jpg" />
</p>
2. Blur image - we should have uniform coins, it means coins should have similar color in center of the money and on the edge.
Why whe should have similary color? Look on point 4 ;).
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/blured.png" width="50%" height="50%" alt="blured.jpg" />
</p>
3. Convert to grey scale, because it easier convert grey scale to binary than RGB 
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/toGrey.png" width="50%" height="50%" alt="grey.jpg" />
</p>
4. Binarization image - it is needed to properly find contures. It is very easy to find contures in binary. In this step we can find first issue. Which binarization algorytm should i used? It is great question. It depends! From the background to money which you want to count. I think you should expirement with all of methods. The best method i think is set a very high binarization threshold and then try to decrease it. When threshold is very big we can easy separate background from our object.
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/binary.png" width="50%" height="50%" alt="binarization.jpg" />
</p>
5. Morphological opening - sometimes is situation when after image bluring or on the orginal image some coins is sticks each other. With sticking is not possible to properly select and count contures. We have to make a small distance bettwen coins. So in this case we use opening. As you can see with opening is a small problem: if you opening too much times one object can disapera. 
<p align="center">
   <img src="https://github.com/GHRik/openCV-exercises/blob/money-counting/money-counting/images/examples/opening.png" width="50%" height="50%" alt="opening.jpg" />
</p>
7. Edge filtering - the next big issue to think about it. It a lot of edge detect algorythm which should i use? The same like above.... It depends. Experiment on your own ;).
8. If you have a selected contures it is easy to count it</br>
9. So the printing only left.

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
