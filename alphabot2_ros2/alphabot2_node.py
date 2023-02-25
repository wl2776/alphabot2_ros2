import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped

import RPi.GPIO as GPIO

from .AlphaBot2 import AlphaBot2

class AlphaBot2Node(Node):
    def __init__(self):
        super().__init__('bot')
        self.cmd_vel_sub = self.create_subscription(TwistStamped, '~/cmd_vel',
                                                    self.process_cmd_vel,
                                                    10)
        self.abot = AlphaBot2()

    def process_cmd_vel(self, msg):
        self.get_logger().info(f'Received {msg}')
        if msg.twist.linear.x > 0:
            self.get_logger().info('Forward')
            self.abot.forward()
        elif msg.twist.linear.x < 0:
            self.get_logger().info('Backward')
            self.abot.backward()
        elif msg.twist.linear.x == 0:
            self.get_logger().info('Stop')
            self.abot.stop()
        elif msg.twist.angular.x > 0:
            self.get_logger().info('Left')
            self.abot.left()
        elif msg.twist.angular.x < 0:
            self.get_logger().info('Right')
            self.abot.right()

    def destroy_node(self):
        self.abot.stop()


def main(args=None):
    rclpy.init(args=args)

    abot2  = AlphaBot2Node()

    rclpy.spin(abot2)

    abot2.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

