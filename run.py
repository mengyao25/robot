import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute, SetPen
import time

class TurtleDraw20(Node):
    def __init__(self):
        super().__init__('turtle_draw_20')
        # 等待服务
        self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        while not self.teleport_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待 teleport_absolute 服务...')
        while not self.pen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('等待 set_pen 服务...')

    def set_pen(self, off):
        req = SetPen.Request()
        req.r, req.g, req.b, req.width = 255, 255, 255, 5
        req.off = off # 1 抬笔(不画线)，0 落笔(画线)
        self.pen_client.call_async(req)
        time.sleep(0.5)

    def teleport(self, x, y, theta):
        req = TeleportAbsolute.Request()
        req.x, req.y, req.theta = x, y, theta
        self.teleport_client.call_async(req)
        time.sleep(0.5)

    def draw_2(self):
        self.get_logger().info('[TurtleDrawer]: Drawing digit 2, step 1...'）    
        self.teleport(2.0, 7.5, 0.0)
        self.set_pen(0)              
        self.teleport(3.0, 8.0, 0.0) 
        self.teleport(4.0, 7.5, 0.0) 
        self.teleport(4.0, 6.5, 0.0) 
        self.teleport(2.0, 4.5, 0.0) 
        self.teleport(4.0, 4.5, 0.0) 
        self.set_pen(1)              

    def draw_0(self):
        self.get_logger().info('[TurtleDrawer]: Drawing digit 0, step 1...')
        self.teleport(6.0, 4.5, 0.0) 
        self.set_pen(0)              
        self.teleport(6.0, 7.5, 0.0) 
        self.teleport(7.0, 8.0, 0.0) 
        self.teleport(8.0, 7.5, 0.0) 
        self.teleport(8.0, 4.5, 0.0) 
        self.teleport(7.0, 4.0, 0.0) 
        self.teleport(6.0, 4.5, 0.0) 
        self.set_pen(1)              

def main(args=None):
    rclpy.init(args=args)
    drawer = TurtleDraw20()
    time.sleep(1)
   
    drawer.draw_2()
    drawer.draw_0()
    
    drawer.get_logger().info('finish')
    drawer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()