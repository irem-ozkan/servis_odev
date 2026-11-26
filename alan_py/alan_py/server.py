import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class AlanServer(Node):

    def __init__(self):
        super().__init__('alan_server')
        self.servis = self.create_service(
            RectangleArea, 'rectangle_area', self.alan_hesapla)
        self.get_logger().info('Alan servisi hazir.')

    def alan_hesapla(self, request, response):
        if request.width < 0 or request.height < 0:
            response.area = 0.0
            response.success = False
            self.get_logger().info('Negatif deger reddedildi.')
        else:
            response.area = request.width * request.height
            response.success = True
            self.get_logger().info(f'Alan: {response.area}')

        return response


def main(args=None):
    rclpy.init(args=args)
    sunucu = AlanServer()
    rclpy.spin(sunucu)
    sunucu.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
