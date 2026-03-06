This repository contains three small robotics-related tasks implemented in Python using libraries such as OpenCV and Matplotlib.
These tasks demonstrate basic concepts in Perception, Localization, and Communication.
1️ Perception Task 
Objective

Detect a colored object in a webcam feed and display its center coordinates.

Tools Used

Python

OpenCV

NumPy

How It Works

The webcam feed is captured using OpenCV.

The frame is converted from BGR → HSV color space.

A color range is defined to detect a specific object (blue in this implementation).

Contours of detected objects are found.

A bounding box is drawn around the object.

The center coordinates of the detected object are printed.




2️ Localization Task 
Objective

Convert GPS latitude and longitude coordinates into local X-Y coordinates relative to a reference point.

Tools Used

Python

Math

Matplotlib

How It Works
How It Works

A reference GPS coordinate is defined as the origin.

Several GPS points are simulated to represent movement.

Differences in latitude and longitude are converted into meters.

The path of movement is plotted using Matplotlib.


3️ Communication Task 
Objective

Simulate sending packets over a network with packet loss and retry mechanism.

Tools Used

Python

Random module

Time module

How It Works

A number of packets are sent sequentially.

Each packet has a 30% chance of being lost.

If a packet is lost, the program retries sending it until successful.
