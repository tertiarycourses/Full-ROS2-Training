import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("my_second_node")
    print("Started the node")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
