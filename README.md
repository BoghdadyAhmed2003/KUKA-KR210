# KUKA KR210 Industrial Manipulator - Full ROS 2 Control & Kinematics Pipeline 🦾🤖

![ROS 2](https://img.shields.io/badge/ROS2-Humble-blue) 
![Linux](https://img.shields.io/badge/Platform-Ubuntu%2022.04-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A comprehensive robotics project featuring the end-to-end development of the **KUKA KR210** industrial arm. This repository demonstrates expertise in robot modeling, physical simulation, and custom kinematic solvers using **ROS 2**.

---

## 📺 Project Showcase (Demos)

| **Gazebo Physics Simulation** | **RViz Visualization** |
|:---:|:---:|
| ![Gazebo](kuka_kr210_gazebo.gif) | ![RViz](kuka_kr210_rviz.gif) |
| *Accurate Dynamics & Collision Detection* | *Real-time Robot State Monitoring* |

| **Kinematics Solver (Python)** | **Joint Trajectory Control** |
|:---:|:---:|
| ![Node](kuka_kr210_control_node.gif) | ![Control](kuka_kr210_control.gif) |
| *Forward/Inverse Kinematics Logic* | *Precision Motion Execution* |

---

## 🛠️ Key Technical Features

### 1. Unified Robot Description (URDF/Xacro)
- Developed a high-fidelity robot model including **Inertial, Visual, and Collision** tags.
- Optimized 3D meshes (STL/DAE) for efficient rendering and physics interaction.

### 2. Physics & Environment (Gazebo)
- Configured Gazebo plugins for sensor integration and motor simulation.
- Verified robot stability and weight-bearing dynamics within a virtual environment.

### 3. Motion Control (ROS 2 Control)
- Implemented `joint_trajectory_controller` for smooth, multi-joint synchronized movement.

### 4. Mathematical Foundation (Kinematics)
- Built a dedicated **Kinematics Node** to handle Forward and Inverse Kinematics.

---

## 👤 Author
**Ahmed Boghdady**
- **LinkedIn:** [Ahmed Boghdady](https://www.linkedin.com/in/boghdady-ahmed-b945b0275)
- **GitHub:** [@BoghdadyAhmed2003](https://github.com/BoghdadyAhmed2003)
