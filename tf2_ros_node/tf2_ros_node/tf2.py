# Publishing transform frame via a python script , from parent_frame to a child_frame 
import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import TransformStamped
# from tf2_ros import Buffer
from tf2_ros.
# import time

class Transform_list(Node):
    def __init__(self):
        super().__init__("trasnform_listner_node")
        self.tf_static_broadcaster = StaticTransformBroadcaster(self)
        # self.publisher = self.create_publisher(TransformStamped,'/tf_frame',10)
        self.timer = 0.05 
        self.timeer = self.create_timer(self.timer,self.control_callback)

    # control method
    def control_callback(self):
        # transform = self.tf_buffer.lookup_transform_core('table1','map',rclpy.time.Time())
        # self.get_logger().info('The transforms has been received %r' %transform)
        self.transform_msg = TransformStamped()
        self.transform_msg.header.stamp = self.get_clock().now().to_msg()
        self.transform_msg.header.frame_id = 'map'
        self.transform_msg.child_frame_id = 'table1'
        self.transform_msg.transform.translation.x = 1.5
        self.transform_msg.transform.translation.y = -0.5
        self.transform_msg.transform.translation.z = 0.92

        self.transform_msg.transform.rotation.x = 0.0
        self.transform_msg.transform.rotation.y = 0.0
        self.transform_msg.transform.rotation.z = 0.0
        self.transform_msg.transform.rotation.w = 0.0

        self.tf_static_broadcaster.sendTransform(self.transform_msg)
        self.get_logger().info('The transforms has been received %r' % self.tf_static_broadcaster)

        

# main function
def main(args=None):
    rclpy.init(args=args)
    transform_listener_node = Transform_list()
    rclpy.spin(transform_listener_node)

if __name__ == '__main__':
    main()



            


