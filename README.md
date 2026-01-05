
# KUKA KR210 Industrial Manipulator  
## Full ROS 2 Control & Kinematics Pipeline 🦾🤖

![ROS 2](https://img.shields.io/badge/ROS2-Humble-blue) 
![Ubuntu](https://img.shields.io/badge/Platform-Ubuntu%2022.04-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A complete robotics simulation and control project for the **KUKA KR210** industrial manipulator using **ROS 2 Humble**.  
This project demonstrates robot modeling, visualization, physics simulation, motion control, and custom kinematics implementation.

---

## 🖼️ Project Overview (Quick Look)

<p align="center">
  <img src="rviz_view.png" width="45%" />
  <img src="gazebo_sim.png" width="45%" />
</p>

<p align="center">
  <img src="control_motion.png" width="45%" />
  <img src="kinematics_demo.png" width="45%" />
</p>

---

## 🛠️ Installation & Build

### 1️⃣ Create Workspace
```bash
mkdir -p ~/manipulators_ws/src
cd ~/manipulators_ws/src
````

### 2️⃣ Clone Repository

```bash
git clone https://github.com/BoghdadyAhmed2003/KUKA-KR210.git
```

### 3️⃣ Build Package

```bash
cd ..
colcon build --packages-select kuka_kr210_arm
source install/setup.bash
```

---

## 🚀 Execution Steps & Demos

### 1️⃣ RViz Visualization

Visualize the robot URDF, joints, and TF tree using RViz.

![RViz Visualization](figs/rviz_view.png)

```bash
ros2 launch kuka_kr210_arm rviz.launch.py
```

---

### 2️⃣ Gazebo Physics Simulation

Spawn the robot in Gazebo with gravity, collisions, and realistic physics.

![Gazebo Simulation](figs/gazebo_sim.png)

```bash
ros2 launch kuka_kr210_arm gazebo.launch.py
```

---

### 3️⃣ Motion Control

Run ROS 2 controllers and execute smooth joint trajectories.

![Motion Control](figs/control_motion.png)

```bash
source install/setup.bash
ros2 launch kuka_kr210_arm controller.launch.py
```

---

### 4️⃣ Custom Kinematics Node

Run the custom Forward and Inverse Kinematics solver.

![Kinematics Results](figs/kinematics_demo.png)

```bash
ros2 run kuka_kr210_arm kinematics_node
```

---

## 📂 Repository Structure

```text
kuka_kr210_arm/
├── urdf/        # Robot Xacro & URDF description files
├── meshes/      # STL / DAE mesh files
├── launch/      # RViz, Gazebo, and controller launch files
├── scripts/     # Custom Python kinematics nodes
└── config/      # ROS 2 controller configurations
```

---

## 👤 Author

**Ahmed Boghdady**
Mechatronics Engineer | Robotics & ROS 2 Developer

* **GitHub:** [https://github.com/BoghdadyAhmed2003](https://github.com/BoghdadyAhmed2003)
* **LinkedIn:** [https://www.linkedin.com/in/boghdady-ahmed-b945b0275/](https://www.linkedin.com/in/boghdady-ahmed-b945b0275/)

---

⭐ If you like this project, don’t forget to star the repository!

```
