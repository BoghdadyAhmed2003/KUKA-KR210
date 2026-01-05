#!/usr/bin/env python3
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    package_name = "kuka_kr210_arm"
    package_share_dir = get_package_share_directory(package_name)
    package_prefix = get_package_prefix(package_name)


    model_arg = DeclareLaunchArgument(
        name='model',
        default_value=os.path.join(package_share_dir, "urdf", "kr210.urdf.xacro"),
        description='Absolute path to the robot URDF/XACRO file'
    )


    env_var = SetEnvironmentVariable(
        "GAZEBO_MODEL_PATH",
        os.path.join(package_prefix, "share") + ":" + os.path.join(package_share_dir, "meshes")
    )

   
    robot_description = ParameterValue(
        Command(['xacro ', LaunchConfiguration("model")]),
        value_type=str
    )

  
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

   
    start_gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gzserver.launch.py")
        )
    )

    start_gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gzclient.launch.py")
        )
    )

   
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'kuka_kr210_arm', 
            '-topic', 'robot_description',
            '-x', '0', '-y', '0', '-z', '0.1' 
        ],
        output='screen'
    )

    return LaunchDescription([
        env_var,
        model_arg,
        robot_state_publisher,
        start_gazebo_server,
        start_gazebo_client,
        spawn_robot
    ])