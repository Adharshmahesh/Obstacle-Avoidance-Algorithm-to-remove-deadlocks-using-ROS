# Obstacle-Avoidance-Algorithm-to-remove-deadlocks-using-ROS

# Requirements

  - ROS Noetic and Gazebo
  - Turtlebot3 Simulator

# Environment where the source code was tested

  - Operating System: Ubuntu 20.04
  - ROS version: ROS Noetic
  - Python version: 3.8.5
  - Extra packages needed: [Turtlebot3 Simulator](https://github.com/ROBOTIS-GIT/turtlebot3_simulations)
  
 # Installation
 
 ```
 cd ~/catkin_ws/src
 git clone https://github.com/McGill-COMP-766-ECSE-683-Assignments/assignment-1-Adharshmahesh.git
 cd ..
 catkin_make
 
 ```
  
 # Running source code
 ```
 After installing ROS Noetic and Turtlebot3 Simulator do the following steps:
 
 Open one terminal window and source it (Type: source ~/catkin_ws/devel/setup.bash)
 Type: roslaunch turtebot3_gazebo turtlebot3world.launch
 
 Open another terminal window (Ctrl + Alt + t) and source it (Type: source ~/catkin_ws/devel/setup.bash)
 Type: roslaunch obstacle_avoid obstacle_avoid.launch
```
# Output

The Gazebo simulator will be opened and the turtlebot will start moving and simultaneously avoiding obstacles as well. The simulation will keep running until it is manually stopped. The simulation can be stopped by pressing Ctrl + C in the opened terminals.
