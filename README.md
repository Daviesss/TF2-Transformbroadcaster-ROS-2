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
     Rotation in a 2D coordinate frame transformation involves changing the orientation of points or objects around a fixed point, often the origin.

    # TRANSLATION :
     In 2D coordinate frames transformation, translation involves shifting an object or point from one position to another without changing its orientation. This is achieved by adding a constant displacement to the x and y coordinates of the object. For instance , if you want to translate a point (x , y) */by (dx , dy), the new coordinates would be (x + dx, y + dy). This process moves the entire object or coordinate system in a specified direction.

  # RUNNING THE ROS 2 NODE :

  clone the package into your created workspace :
     
```
   https://github.com/Daviesss/TF2-Transformbroadcaster-ROS-2.git
```

NOTE : Make sure you build the package after cloning into your workspace 

```
  colcon build
```

# RUNNING THE NODE AND EXPLANAITION WHAT EVERY LINE OF THE NODE DOES 

```
  ros2 run tf2_ros_node tf2_publisher
```


![Screenshot from 2023-12-10 11-01-34](https://github.com/Daviesss/TF2-Transformbroadcaster-ROS-2/assets/97457075/66b00b19-8122-4bff-b97b-6f11e92c56cd)


  
     
