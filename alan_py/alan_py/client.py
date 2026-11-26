import sys
import rclpy
from rclpy.node import Node
from alan_interfaces.srv import RectangleArea


class AlanClient(Node):

    def __init__(self):
        super().__init__('alan_client')
        self.istemci = self.create_client(
            RectangleArea, 'rectangle_area')

        while not self.istemci.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')

    def istek_gonder(self, genislik, yukseklik):
        istek = RectangleArea.Request()
        istek.width = genislik
        istek.height = yukseklik
        return self.istemci.call_async(istek)


def main(args=None):
    if len(sys.argv) != 3:
        print('Kullanim: ros2 run alan_py client genislik yukseklik')
        return

    genislik = float(sys.argv[1])
    yukseklik = float(sys.argv[2])

    rclpy.init(args=args)
    istemci = AlanClient()

    sonuc = istemci.istek_gonder(genislik, yukseklik)
    rclpy.spin_until_future_complete(istemci, sonuc)

    yanit = sonuc.result()

    if yanit.success:
        print(f'Dikdortgen alani: {yanit.area}')
    else:
        print('Hata: Negatif deger girilemez.')

    print(f'Success: {yanit.success}')

    istemci.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
