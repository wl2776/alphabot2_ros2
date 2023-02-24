import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped

import RPi.GPIO as GPIO

from AlphaBot import AlphaBot

class AlphaBot2(Node):
    def __init__(self):
        super().__init__('alphabot2')
        self.cmd_vel_sub = self.create_subscription(
            TwistStamped,
            '/cmd_vel',
            self.process_cmd_vel,
            10)
        self.abot = AlphaBot()

        self.IR = 18
        self.PWM = 50
        self.n=0

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(IR,GPIO.IN,GPIO.PUD_UP)


    def process_cmd_vel(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def destroy_node(self):
        self.abot.stop()
        GPIO.cleanup()


def main(args=None):
    rclpy.init(args=args)


    abot2  = AlphaBot2()

    rclpy.spin(abot2)

    abot2.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
