import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('my_third_node')

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    print("Started the node")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
