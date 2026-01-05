from setuptools import setup
import os
from glob import glob

package_name = 'kuka_kr210_arm'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # ملفات تعريف الحزمة الأساسية
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # تثبيت ملفات الـ Launch
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        
        # تثبيت ملفات الـ URDF و Xacro
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        
        # تثبيت ملفات الإعدادات (Config) مثل ملفات RVIZ أو ملفات التحكم
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        
        # تثبيت ملفات الـ Rviz (لو موجودة في مجلد منفصل)
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),

        # تثبيت ملفات المجسمات (Meshes) - مهم جداً لظهور الروبوت
        (os.path.join('share', package_name, 'meshes/collision'), glob('meshes/collision/*')),
        (os.path.join('share', package_name, 'meshes/visual'), glob('meshes/visual/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='noshluk2@gmail.com',
    description='KUKA KR210 Robot Arm Package for ROS 2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'trajectory_exec = kuka_kr210_arm.1_controller_test:main',
            'inverse_kinematics = kuka_kr210_arm.2_inverse_kinematics_solution:main',
            'sqaure_actionClient = kuka_kr210_arm.3_action_client_interface:main',
            'trajectory_publisher = kuka_kr210_arm.robot_trajectory_publisher:main',
        ],
    },
)