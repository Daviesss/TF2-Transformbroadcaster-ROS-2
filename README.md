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

Now open rviz2 while the command node is running 

```
  rviz2
```

Set the fixed frame to map and add the tf tag using the add tag and the tf name on rviz2, below the left hand side of rviz2 . You will see a transform link from "map" which is the fixed_frame to "child_frame_name" which is the child frame . You can name the child_frame to what you want . Normally it is always a sensor frame name which is attached to the fixed_frame the origin of the robot. In this scenario , we named it "child_frame_name" which is the child_frame name , map is the fixed frame. So its a transform going from map->child_frame_name.

# NODE EXPLANATION 







  
     
