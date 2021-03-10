import rclpy
from time import sleep
from std_msgs.msg import String

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('my_fourth_node')
    publisher = node.create_publisher(String, 'greeting', 10)

    msg = String()
    i = 0
    while rclpy.ok():
        msg.data = 'Hello World: %d' % i
        i += 1
        node.get_logger().info('Publishing: "%s"' % msg.data)
        publisher.publish(msg)
        sleep(0.5)  # seconds

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()