import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__('my_fourth_node')
        self.publisher_ = self.create_publisher(String, "greetings", 10)
        self.create_timer(0.2, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.i += 1
        
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    print("Started the node")
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
