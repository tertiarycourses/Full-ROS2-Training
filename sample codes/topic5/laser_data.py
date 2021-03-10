import rclpy
from sensor_msgs.msg import LaserScan	

def callback(msg):	
	print('s1 [0]')				
	print(msg.ranges[0])	

	print('s2 [90]')
	print(msg.ranges[90])

	print('s3 [180]')
	print(msg.ranges[180])

	print('s4 [270]')
	print(msg.ranges[270])

	print('s5 [359]')
	print(msg.ranges[359])

def main(args=None):
	rclpy.init(args=args)
	node = rclpy.create_node("laser_data")	
	sub = node.create_subscription(LaserScan,"scan", callback,10)

	while rclpy.ok():
        rclpy.spin_once(node)
	
if __name__ == '__main__':
	main()
