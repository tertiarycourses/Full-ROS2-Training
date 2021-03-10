import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__('my_eighth_node')
        self.subscription = self.create_subscription(
            String,
            'greeting',
            self.callback,
            10)
        self.subscription  # prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    sub = MyNode()
    rclpy.spin(sub)
    sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()