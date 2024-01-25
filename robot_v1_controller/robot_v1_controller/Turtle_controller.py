#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class turtle_node(Node):
    def __init__(self):
        super().__init__("turtle_close_node1")
        self.get_logger().info("The turtle_controller Node has been started")
        # Nodun ne olduğu ile ilgili detayların hepsi kendi init sınıfının içinde tanımlanmalıdır.

        #+------------------------- 
        # hem subscription hemde publisher eklenmelidir.| önceki kodlarla aynı.
        self.pose_sub = self.create_subscription(Pose,"/turtle1/pose",self.callback, 10)
        self.vel_pub = self.create_publisher(Twist,"/turtle1/cmd_vel",10)

    def callback(self, position:Pose):
        # burada bir mesaj olutşruacağız ve pose subscriptipnu sağlanana kadar kapalı bir loop gibi çalışmaya devam edecektir.
        msg = Twist()
        if (position.x)>9.0 or (position.x<2.0) or (position.y<2.0) or (position.y>9.0):
            msg.linear.x = 1.0
            msg.angular.z = 0.75
            self.get_logger().info("status :: TURN")
        else:  
            msg.angular.z  = 0.0
            msg.linear.x = 3.0
            self.get_logger().info("status :: FORWARD")
        # buradaki kondisyon ile objenin 11x11 lik çerçeveden dışarı çıkmaması sağlanmış oldu.
        # kondisyonun ifadesine göre de daha farklı eklemeler ifadeler düşünülebilir.
             
        self.vel_pub.publish(msg)

def main(args= None):
    rclpy.init(args=args)
    node_1 = turtle_node()
    rclpy.spin(node_1)

    rclpy.shutdown()


if __name__=='__main__':
    main()