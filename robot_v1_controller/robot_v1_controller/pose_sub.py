#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


# ilgili topic direkt turtlesim içinde var. biz bunuda topic info yaparak son kısmındaki yere bakıyoruz ve alıyoruz.

# // ros2 interface show message type  > bize msg içeriği ile ilgili bilgi verecektir. Bu bilgilere dayanarak mesaj içerğini ineleyebilriiz.


# nodelar direkt class oriented object olarak alınakcaktır.
class pose_subcription(Node):
    def __init__(self):
        super().__init__("Turtlesim_pose_estimation")
        self.pose_sub_ = self.create_subscription(Pose,"/turtle1/pose",self.callback, 10)
        # init içinde tanımlandığı için direkt self tanımıı yapmayı unutmamak lazım // fonksyonlar içinde dahil.

    def callback(self, msg:Pose):
        # msg tanımındaki pose anlamında dikkat. direkt olarak message ögesinin bir pose olduğunu ifade etmiş olduk.
        # -> bir önceki örenkte de direkt önce msg = twist olarka ifade etmiştik, aynısını yine yapabilirdik.
        self.get_logger().info("X- " + str(msg.x) + "     " + "Y-"+ str(msg.y))
        # direkt message ögesinin kendisini yazdırabiliyoruz.


def main(args = None):
    rclpy.init(args=args)
    node_2 = pose_subcription()

    rclpy.spin(node_2)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
