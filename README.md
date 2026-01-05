# KUKA KR210 Robot Arm Simulation - ROS 2

This repository contains a professional **URDF** description and simulation setup for the **KUKA KR210** industrial manipulator. Developed using **ROS 2**, this project focuses on accurate kinematic modeling and visualization in **RViz** and **Gazebo**.

## 🚀 Key Features
- **Accurate Kinematics**: Complete URDF model with 6 Degrees of Freedom (DOF).
- **Physical Properties**: Precise definition of Inertial tensors, Mass, and Center of Gravity for realistic physics.
- **Visuals & Collision**: High-quality STL/DAE meshes for both aesthetic visualization and efficient collision detection.
- **ROS 2 Launch System**: Optimized launch files for quick environment setup.

## 📂 Repository Structure
- `urdf/`: Contains the `.urdf` and `.xacro` files for the robot description.
- `meshes/`: 3D models for the robot links (Visual & Collision).
- `launch/`: Python launch files to run the simulation.
- `config/`: Configuration files for controllers and RViz.

## 🛠️ Installation & Usage
### Prerequisites
- ROS 2 (Humble or Iron recommended)
- `colcon` build tool

### Build the Package
```bash
cd ~/ros2_ws/src
git clone [https://github.com/BoghdadyAhmed2003/KUKA-KR210.git](https://github.com/BoghdadyAhmed2003/KUKA-KR210.git)
cd ..
colcon build --packages-select kuka_kr210_arm
source install/setup.bash
