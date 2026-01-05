import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class TrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('trajectory_publisher_node')
        self.publisher_ = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        self.timer = self.create_timer(4.0, self.send_trajectory) 
        self.state = 0
        self.get_logger().info('KUKA KR210 Active Motion Node Started!')

    def send_trajectory(self):
        msg = JointTrajectory()
        msg.joint_names = [
            'joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6',
            'right_gripper_finger_joint', 'left_gripper_finger_joint'
        ]

        point = JointTrajectoryPoint()
        
        if self.state == 0:
          
            point.positions = [1.0, -0.6, 0.4, 0.7, 0.5, 1.2, 0.03, 0.03]
            self.state = 1
            self.get_logger().info('Action: Expanding and Opening Gripper')
        elif self.state == 1:
            
            point.positions = [-1.0, -0.2, -0.3, -0.7, -0.5, -1.2, 0.0, 0.0]
            self.state = 2
            self.get_logger().info('Action: Twisting and Closing Gripper')
        else:
           
            point.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            self.state = 0
            self.get_logger().info('Action: Returning to Home Position')

     
        point.time_from_start = Duration(sec=1, nanosec=500000000)
        msg.points.append(point)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()