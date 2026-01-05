حاضر يا باشمهندس 
# KUKA KR210 Industrial Manipulator  
## Full ROS 2 Control & Kinematics Pipeline 🦾🤖

![ROS 2](https://img.shields.io/badge/ROS2-Humble-blue)
![Ubuntu](https://img.shields.io/badge/Platform-Ubuntu%2022.04-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A complete robotics simulation and control project for the **KUKA KR210** industrial manipulator using **ROS 2 Humble**.  
The project covers robot modeling, visualization, physics simulation, control, and custom kinematics implementation.

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

Visualize the robot URDF, joints, and TF tree.

```bash
ros2 launch kuka_kr210_arm rviz.launch.py
```

🎥 **Demo Video:**

> *(Add RViz demo video link here)*

---

### 2️⃣ Gazebo Physics Simulation

Spawn the robot in Gazebo with gravity and collision enabled.

```bash
ros2 launch kuka_kr210_arm gazebo.launch.py
```

🎥 **Demo Video:**

> *(Add Gazebo simulation video link here)*

---

### 3️⃣ Motion Control

Run ROS 2 controllers and execute joint trajectories.

```bash
source install/setup.bash
ros2 launch kuka_kr210_arm controller.launch.py
```

🎥 **Demo Video:**

> *(Add controller motion video link here)*

---

### 4️⃣ Custom Kinematics Node

Run the custom Forward & Inverse Kinematics implementation.

```bash
ros2 run kuka_kr210_arm kinematics_node
```

🎥 **Demo Video:**

> *(Add kinematics demo video link here)*

---

## 📂 Repository Structure

```text
kuka_kr210_arm/
├── urdf/        # Robot Xacro & URDF files
├── meshes/      # STL / DAE mesh files
├── launch/      # RViz, Gazebo, controller launch files
├── scripts/     # Python kinematics nodes
└── config/      # Controller configurations
```

---

## 👤 Author

**Ahmed Boghdady**
Mechatronics Engineer | Robotics & ROS Developer

* **GitHub:** [https://github.com/BoghdadyAhmed2003](https://github.com/BoghdadyAhmed2003)
* **LinkedIn:** [https://www.linkedin.com/in/boghdady-ahmed-b945b0275/](https://www.linkedin.com/in/boghdady-ahmed-b945b0275/)

---

### 📌 Notes

* Tested on **Ubuntu 22.04 + ROS 2 Humble**
* Designed for learning **industrial manipulators, kinematics, and ROS 2 control**
* Easily extendable to MoveIt 2 and advanced planning

---

⭐ If you like this project, don’t forget to star the repository!

```
