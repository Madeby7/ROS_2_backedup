import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

# twist tipinde bir velocity topiği olduğunu biliyoruz bu turtlesimin.
# bu topiğe bağlı olan bir publisher oluşturaacağız ki müdehale edebileim.


class draw_circle_node(Node):
    # buraya dikkat, burada bir node çalıştırıyoruz, bu noktada inheritance veerirken bunu Node ana sınfından vermemiz öneliydi.
    def __init__(self):
        super().__init__("drawing_a_circle")
        self.get_logger().info("the drawing circle in turtule is starting")
        self.cmd_vel_pub_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        # burada sistem komutu ve bir publisher yayını yapılması içingerekli parametreler ve istekler var.
        #publisher isteklerinde önce type, sonrasında ilgili topiğin adı sonrasında bir alan numarası // 10 ideal dendi.
        # -> burası aslında publisherın confiği gibi diyebiliriz. mesaj içeriği ayrı şekilde aşağıda verdiğimiz objeden oluyor.
        

        self.timer_ = self.create_timer(0.5,self.circle_act)
        # timer sistemini ayarladık, bir değişkene atanmasında problem yok, sonuçta create timerdan referans alıyoruz.
        self.get_logger().info("Drawing Node tool has been started")
    # --> buradaki tüm çalışmaların hepsi init içinde gerçekleştirildi. self değerinde direkt olarak ilgili node objesinin kendisine atanmış oldu.
        
    
    def circle_act(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)
        # self.cmd_vel_pub değişkeni create pbulisher dan üretildi. tip ve topic ismi belli yani.
        # bunu pbulish ederken içeriğindeki mesajıda circle actin içinde verdik ki turutliime ne yapacağını söylesin.
        # bunun detaylarını, mesaj içeriğinde ne olmasının gerektiğini interface show kısmından öğrendik ve msg içerğinde belirttik.
        # msg değişkenini oluşturuken ne tipte olduğunu öğrenmişti, direkt bu değişkene ne olduğunu fonksiyonun ilk satırında söyledik.



def main(args=None):
    rclpy.init(args=args)
    node_1 = draw_circle_node()
    rclpy.spin(node_1)
    rclpy.shutdown

if __name__ == '__main__':
    main()