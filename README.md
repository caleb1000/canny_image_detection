# canny_image_detection
This is my experiment with canny image detection in python. Currently this program only applys a Gaussian filter, greyscale conversion, and the average of the sobel x and y operators.

https://en.wikipedia.org/wiki/Canny_edge_detector <br />

TO:DO <br />
-Use Numpy <br />
-Only open target file once <br />
-Take in command line args <br />
-Lower bound cut-off suppression <br />
-Double threshold <br />
-Edge tracking by hysteresis <br />

Original Image <br />
![image](https://user-images.githubusercontent.com/30327564/197315137-20a25181-5c3a-4861-882f-9d78e3747c0f.png)

Blurred Greyscale <br />
![image](https://user-images.githubusercontent.com/30327564/197327682-8fe82e52-85b8-4d43-b12a-b6f25b85e114.png)<br />

Sobel X <br />
![image](https://user-images.githubusercontent.com/30327564/197327706-6283a8d3-3ffd-4cb4-96f1-d7a0b694b738.png) <br />

Sobel Y <br />
![image](https://user-images.githubusercontent.com/30327564/197327720-2f597585-34a0-4dbc-bb3c-1fb91606e306.png) <br />

Sobel Average <br />
!![image](https://user-images.githubusercontent.com/30327564/197327672-ec3b8165-5dda-4cb9-833f-3c4a25c37399.png) <br />
