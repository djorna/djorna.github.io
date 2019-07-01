Title: A Guide to Learning Modern vSLAM 
Date: 2019-03-25 15:40 
Modified: 2019-06-17 20:39
Category: Education
Tags: Computer Vision, SLAM
Slug: vslam_guide
Authors: David Jorna
Summary: A simple explanation of vSLAM.
Featured_Image: images/lsd_slam.jpg

Visual Simultaneous Localization and Mapping (vSLM) is a rapidly accelerating area of research that will have an important impact in modern technology. It is a key ingredient of what makes self driving cars, autonomous drones, and augmented reality possible.

## A Brief History of SLAM


## Terminology
For mere mortal, among which I count myself, the jargon can be a bit overwhelming at first.


* Structure from motion (SfM)


## The 

## Papers
Visual SLAM is a complex subject, so in order to get a better understanding of it, you can't avoid a bit of heavy reading. Once you have a decent understanding of the key terminology, I recommend reading the following papers to start. The state of the art in vSLAM is every-changing, so which I will try to keep this list up-to-date, it is by no means exhaustive.

* LSD-SLAM
* ORB-SLAM
* CNN-SLAM

In future posts I plan to describe some of these papers in depth.


## Types of vSLAM

### Sparse vs. Dense
"Sparse" and "Dense" refer to exactly what you'd expect: whether the points in the resulting 3D map are close or far apart. Sparse vSLAM is good enough for localization, but is not sufficent for applications which require a full 3D-model of the environment, such as robotic navigation, or 

### Direct vs Keypoints
The old-school (and currently state-of-the-art) method of doing vSLAM is by extracting keypoints from image using feature descriptors. These work by...

In contrast, direct methods operate directly on the pixels of the image. The advantage of this method is that it has the potential to be more robust, and generate denser maps. However, the problem with current direct methods, such as LSD-SLAM is that they are highly sensitive to image noise, so their use is mostly restricted to specialized high-quality cameras.

## Further Reading
vSLAM is an active area of research, so to really understand it, you will need to read some papers.

* LSD-SLAM
* ORB-SLAM
* CNN-SLAM