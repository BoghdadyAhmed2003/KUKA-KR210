import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    package_share_dir = get_package_share_directory("kuka_kr210_arm")
    urdf_file = os.path.join(package_share_dir, "urdf", "kr210.urdf")
    
    controller_file = os.path.join(package_share_dir, "config", "jtc.yaml")
    
    
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gazebo", "-s", "libgazebo_ros_factory.so"],
                output="screen",
            ),
   
            Node(
                package="gazebo_ros",
                executable="spawn_entity.py", 
                arguments=["-entity", "kuka_kr210_arm", "-topic", "robot_description"],
            ),
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                output="screen",
                parameters=[{'robot_description': robot_desc}], 
            ),
            
            Node(
                package="controller_manager",
                executable="ros2_control_node",
                parameters=[{'robot_description': robot_desc}, controller_file],
                output="screen",
            ),
            
            
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["joint_state_broadcaster"],
            ),

            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["joint_trajectory_controller"],
            )
        ]
    )