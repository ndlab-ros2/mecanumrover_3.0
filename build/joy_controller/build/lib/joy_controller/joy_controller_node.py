from rclpy.node import Node
import rclpy

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyControllerNode(Node):
    def __init__(self):
        super().__init__("joy_mecanumrover_controller")
        self.publisher_ = self.create_publisher(
            Twist, "rover_twist", 10
        )
        self.subscriber_ = self.create_subscription(
            Joy,"joy", self.callback_joy, 10)
        self.get_logger().info("Started.")
    
    def callback_joy(self,msg):
        twist_msg = Twist()
        linear_x = msg.axes[1]*1
        angular_z = msg.axes[2]*1
        twist_msg.linear.x = linear_x
        # twist_msg.angular.z = angular_z
        self.publisher_.publish(twist_msg)

        # self.get_logger().info("linear_x: %f angular_z: %f" % (linear_x, angular_z))

def main(args=None):
    rclpy.init(args=args)
    node = JoyControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()