#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node

#-> node extension olarak inceleme kütüphanesi




# nodelar direkt class oriented object olarak alınakcaktır.
class node_1(Node):
    def __init__(self):
        super().__init__("First_Node")
        # super ile bu class obejsinin kendisine ismini verdik. // First node

        # create time ve spin kombinasyonu ile de sürekli döngüye alabileceğimiz bir sistem oluşturduk.
        self.counter_1 = 0

        self.create_timer(0.7, self.get_call)
    

    def get_call(self):
        self.get_logger().info("Goodbye ROS2!" + str(self.counter_1))
        self.counter_1 += 1

def main(args = None):
    rclpy.init(args=args)
    node = node_1()
    # ilgili node burada çağrılacaktır. Çalışma alanı burasıdır.

    rclpy.spin(node)
    # Nodun hala terminalde aktif olarak çalışmasını sağlar.

    rclpy.shutdown()

if __name__ == '__main__':
    main()



