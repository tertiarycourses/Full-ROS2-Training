import rclpy
from geometry_msgs.msg import Twist	

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node("turtlebot3_move")	
    # pub = node.create_publisher(Twist,"/turtle1/cmd_vel",10)
    pub = node.create_publisher(Twist,"/cmd_vel",10)
    move = Twist()
    while rclpy.ok():
        move.linear.x = 0.1
        move.angular.z = 0.0
        pub.publish(move)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


