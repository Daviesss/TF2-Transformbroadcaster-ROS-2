# TF2-Transformbroadcaster-ROS-2
This package describes how to broadcast a static transform in ROS 2 using python.


# PUBLISHING TF2 TRANSFORM BROADCASTER USING PYTHON

 We will be using ROS 2 concepts . We start first talking about Cor-ordinate systems in robotics. 

# COORDINATE SYSTEMS
A coordinate frame describes the position of points with respect to an origin by means of a collection of orthogonal axes that intersect at that point. This point is known as the origin. Although the terms reference frame and coordinate frame can be used interchangeably. There are types of coordinate frames in robotics which are 2D coordinate frame and also 3D coordinate frame.

# 2D COORDINATE FRAMES
The Cartesian plane, which utilizes location coordinates of the form (x, y). A coordinate frame in 2D space is a set of two vectors having unit length and that make a right angle with one another. We have the x and y plane since our robot in relation to the ground. A 2D coordinate transformation consists of three basics which are 

- scale change.
- rotation. 
- translation.

    # SCALE CHANGE :
    This refers to the modification of the size of an object or space. This transformation involves adjusting the distances between points in the x and y directions. Scalling can be uniform, where x and y dimensions are scaled equally, or non-uniform, where the scalling factors may differ for each axis.

    # ROTATION :
