import rclpy

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node("my_first_node")
    print("Started the node")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
