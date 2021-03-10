import rclpy
from std_msgs.msg import String

g_node = None

def callback(msg):
    global g_node
    g_node.get_logger().info(
        'I heard: "%s"' % msg.data)

def main(args=None):
    global g_node
    rclpy.init(args=args)

    g_node = rclpy.create_node('my_seventh_node')

    subscription = g_node.create_subscription(String, 'greeting', callback, 10)

    while rclpy.ok():
        rclpy.spin_once(g_node)

    g_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()