Article titles:
* The Definitive guide to ROS
* How to ROS
* Your first ROS Project
* WTF is SLAM?


# WTF is SLAM??

In robotics, SLAM stands for Simultaneous Localization and Mapping. But if your're reading this, you probably already knew that. However, I've you've ever taken the dive into the mysterious world of SLAM, you may have found that this question is not so simple as you may have first imagined. In this article, we wil go over the basics of SLAM, from Kalman filters to Visual SLAM, and everything in between.

## Where am I?

Imagine you're a mobile robot or unmanned ground vehicle (UGV) and you want to know your GPS coordinates. You have a GPS, a depth camera, wheel encoders, and an inertial measurement unit (IMU). What do you do?

When faced with this task for the first time, you may come up with an algorithm that looks something like this:

    readGPS()

If only life were this simple. The problem with this approach is that GPS readings can have a tolerance of up to a whole meter! Maybe we can use some of the other tools in out toolbox to help...

## Enter the Kalman Filter



