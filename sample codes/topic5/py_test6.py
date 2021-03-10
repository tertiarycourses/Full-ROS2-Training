import rclpy
from geometry_msgs.msg import Twist	

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node("turtle_move")	
    pub = node.create_publisher(Twist,"/turtle1/cmd_vel",10)
    move = Twist()
    while rclpy.ok():
        move.linear.x = 0.5
        move.angular.z = 0.8
        pub.publish(move)

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
