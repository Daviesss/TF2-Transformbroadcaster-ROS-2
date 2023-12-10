# Publishing transform frame via a python script , from parent_frame/fixed_frame to a child_frame  
# import packages needed 
import rclpy 
from rclpy.node import Node 
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster 


class Transform_list(Node):
    def __init__(self):
        super().__init__("trasnform_listner_node")
        self.Transform_broadcast = TransformStamped()
        self.broadcaster = TransformBroadcaster(self)
        self.timer = 0.05 
        self.timeer = self.create_timer(self.timer,self.control_callback)

    # control method
    def control_callback(self):
        self.Transform_broadcast.header.stamp = self.get_clock().now().to_msg()
        self.Transform_broadcast.header.frame_id = 'map' # origin frame/fixed_frame name 'map'
        self.Transform_broadcast.child_frame_id = 'child_frame_name' # child_frame/frame which is attaced to the origin frame/world_frame
        self.Transform_broadcast.transform.translation.x = 1.5
        self.Transform_broadcast.transform.translation.y = -0.5
        self.Transform_broadcast.transform.translation.z = 0.92
        
        # rotation of the frame 
        self.Transform_broadcast.transform.rotation.x = 0.0
        self.Transform_broadcast.transform.rotation.y = 0.0
        self.Transform_broadcast.transform.rotation.z = 0.0
        self.Transform_broadcast.transform.rotation.w = 1.0

        self.broadcaster.sendTransform(self.Transform_broadcast)
        self.get_logger().info('The transforms has been received %r' % self.broadcaster)

        

# main function
def main(args=None):
    rclpy.init(args=args)
    transform_listener_node = Transform_list()
    rclpy.spin(transform_listener_node)

if __name__ == '__main__':
    main()
