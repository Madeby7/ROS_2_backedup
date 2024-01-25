#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
#-------------------------------------
from turtlesim.srv import SetPen
# -> serv oalrak hangi uygulama ile kullanılacaksa servisi entegre ediliyor sisteme
from functools import partial
# -> ileriki requestin tanımlanırken kullandıpımız bir tool.



class turtle_node(Node):
    def __init__(self):
        super().__init__("turtle_close_node1")
        self.get_logger().info("The turtle_controller Node has been started")
        self.pose_sub = self.create_subscription(Pose,"/turtle1/pose",self.callback, 10)
        self.vel_pub = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.previous_x_= 0

    def callback(self, position:Pose):
        msg = Twist()
        if (position.x)>9.0 or (position.x<2.0) or (position.y<2.0) or (position.y>9.0):
            msg.linear.x = 1.0
            msg.angular.z = 0.75
            #self.get_logger().info("status :: TURN")
        else:  
            msg.angular.z  = 0.0
            msg.linear.x = 3.0
            #self.get_logger().info("status :: FORWARD")
        
        self.vel_pub.publish(msg)

        # service callback ile service işlemlerini entegresyonu direkt node callback fonksyonu içinde sağlanabilir.
        if position.x > 5.5 and self.previous_x_<=5.5:
            self.get_logger().info("The turtle on the right:: RED")
            self.service_call_set_pen(254,0,0,5,0)
            self.previous_x_ = position.x
            """
            # kondisyonun previous eklentisi sadece geçişler arasinda değişiklik olacağı zaman çalışacak şekilde ayarlandı.
                -> bu sayede sürekli olarak service call yapılmamış olacak ve performans açısından kolaylık sağlanacaktır.

            """
        elif position.x <= 5.5 and self.previous_x_ > 5.5:
            self.get_logger().info("The turtle on the left:: GREEN")
            self.service_call_set_pen(0,254,0,5,0)
            self.previous_x_ = position.x
        else:
            pass



    def service_call_set_pen(self,r,g,b,width,off):
        client = self.create_client(SetPen,"/turtle1/set_pen")

        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the services....")
            # -> while not içinde service bağlantısı sağlanamdığı sürece bi log bilgisi ekrana yansıyacaktır.
            # bu şekilde service bağlantısı kesilmiş mi kesilmemiş mi kontrol edilebilir, çok mantıklı bir sorgudur.


        # şimdi service için request ayarlamansına geldi.
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        # -> future aslında ileride olacak bir işlemin şimdiden hazırlanması.
        #   yani ileride yapmak istediğimiz çağrılacak requestin değişkenleri ile beraber tutulması için ve çağrılması için hazırladık
        future.add_done_callback(partial(self.future_callback_))
    
    def future_callback_(self,future):
        # service yanıtlandığında bu fonskyon devreye girecektir. /-/ işte burada responsu oluşturacağız. 
        # mantıkende callback çağrısına cevap vermeyen bir service den başka zaman response beklemekte saçma olacaktır.
        try:
            response = future.result()
            # interface showda öğrenmiştik herhangi bir response yok bu set pende o yüzden herhangi bir dönüt olarka kullanmadık.

        except Exception as e:
            self.get_logger().error("service call failed :: %r" %(e,))
        # direkt try ve except içerisidne bunu eridk ki belirli bir hata durumunda direkt exceptionu belirtsin.
        

def main(args= None):
    rclpy.init(args=args)
    node_1 = turtle_node()
    rclpy.spin(node_1)

    rclpy.shutdown()


if __name__=='__main__':
    main()