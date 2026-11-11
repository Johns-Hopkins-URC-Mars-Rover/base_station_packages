
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from xbox360controller import Xbox360Controller

controller = Xbox360Controller(0, 0.1)

class XboxControllerPublisher(Node):
    def __init__(self):
        super().__init__('xbox_controller_pub')
        self.publisher_ = self.create_publisher(Twist, '/diff_drive_controller/cmd_vel_unstamped', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        speed = -controller.axis_l.y * 50
        turn = controller.axis_r.x * 50
        data = Twist()
        data.linear.x = speed
        data.angular.z = turn
        self.publisher_.publish(data)

def main(args=None):
    rclpy.init(args=args)

    pub = XboxControllerPublisher()

    rclpy.spin(pub)

    pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()