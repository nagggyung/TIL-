## Image of Pillow and OpenCV 

When the image file is read with the OpenCV function imread(), the order of colors is BGR (blue, green, red). <br>
On the other hand, in Pillow, the order of colors is assumed to be RGB (red, green, blue).<br>
Therefore, if you want to use both the Pillow function and the OpenCV function, **you need to convert BGR and RGB.**

You can use the OpenCV function **cvtColor()** or simply change **the order of ndarray**

### 1) OpenCV is BGR, Pillow is RGB
When reading a color image file, OpenCV **imread()** reads as a **NumPy array ndarray** of row(height) x column(width) x color(3).
The order of color is BGR(blue, green, red)

The OpenCV function imwrite() that saves an image assumes that the order of colors is BGR, so it is saved as a correct image.

```c 
import cv2
import numpy as np
from PIL import Image

im_cv = cv2.imread('data/src/lena.jpg')

cv2.imwrite('data/dst/lena_bgr_cv.jpg', im_cv)
```

![image](https://user-images.githubusercontent.com/74478432/138106168-82490f80-aba7-4687-a420-5f1f82db5f82.png)

When the performing image processing with Pillow, you can convert ndarray to a PIL.Image object with Image.fromarray(), but in Pillow the color order assumes RGB(red, green, blue).

Therefore, if the ndarray of the image read by openCV imread() is converted to a PIL.Image object and saved, the image with the wrong color is saved.


```c 
pil_img = Image.fromarray(im_cv)
pil_img.save('data/dst/lena_bgr_pillow.jpg')
```

![image](https://user-images.githubusercontent.com/74478432/138106610-49f48cb9-0daf-4664-860c-1509b7ab0988.png)


If you want to conver ndarray and PIL.Image objects to use both Pillow and OpenCV functions, you need to convert BGR to RGB.


### 2) Convert BGR and RGB with OpenCV function cvtColor()

Various color spaces such as RGB, BGR, HSV can be mutually converted using OpenCV function cvtColor()

```c 
cv2.cvtColor(img, code)
```

When code is cv2.COLOR_BGR2RGB, BGR is converted to RGB.

When converted to RGB, it will be saved as a correct image even if it is saved after being converted to a PIL.Image object.

```c 
im_rgb = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)

Image.fromarray(im_rgb).save('data/dst/lena_rgb_pillow.jpg')
```

![image](https://user-images.githubusercontent.com/74478432/138107417-34626153-f17e-4830-bcda-88c8bfbb2686.png)


When converted to RGB and saved with OpenCV imwrite(), it will be an incorrect color image

```c 
cv2.imwrite('data/dst/lena_rgb_cv.jpg', im_rgb)
```

![image](https://user-images.githubusercontent.com/74478432/138107597-3023d68a-6644-40b1-ac3d-be94ff4b1396.png)


The parameter code when converting from RGB to BGR is cv2.COLOR_RGB2BGR.<br>
Use this when reading an image file as a PIL.Image, convert it to ndarray, and save it using OpenCV imwrite().

```c 
im_pillow = np.array(Image.open('data/src/lena.jpg'))

im_bgr = cv2.cvtColor(im_pillow, cv2.COLOR_RGB2BGR)

cv2.imwrite('data/dst/lena_bgr_cv_2.jpg', im_bgr)
```

### 3) Convert BGR and RGB without using cvtColor()

Convert BGR and RGB can be realized without using cvtColor().

There are several ways, for examples as follows

```c 
im_bgr = cv2.imread('data/src/lena.jpg')

im_rgb = im_bgr[:, :, [2, 1, 0]]
Image.fromarray(im_rgb).save('data/dst/lena_swap.jpg')

im_rgb = im_bgr[:, :, ::-1]
Image.fromarray(im_rgb).save('data/dst/lena_swap_2.jpg')
```


## Reference 

https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/


