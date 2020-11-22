import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyNode(Node):

    def __init__(self):
        super().__init__('my_fifth_node')
        self.subscription = self.create_subscription(String,'greetings',self.listener_callback,10)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    print("Started the node")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
