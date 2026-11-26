# ROS 2 – RectangleArea Servisi

## 1. Projenin Amacı

ROS 2 kullanılarak dikdörtgenin alanını hesaplayan bir servis geliştirilmiştir. Sunucu ve istemci arasındaki iletişim özel bir servis arayüzü üzerinden sağlanmıştır.

## 2. Kullanılan Teknolojiler

- Ubuntu
- ROS 2
- Python (rclpy)

## 3. Paketler ve Çalışma Mantığı

- **alan_interfaces:** `RectangleArea.srv` dosyasında genişlik (`width`), yükseklik (`height`) ve alan (`area`) değerleri `float64` olarak tanımlanmıştır. Yanıta bonus kapsamında `bool success` alanı eklenmiştir.
- **alan_py:** `server.py` dosyasında genişlik ve yükseklik çarpılarak alan hesaplanmaktadır. `client.py` dosyasında komut satırından alınan iki sayı sunucuya gönderilmekte ve sonuç görüntülenmektedir.

## 4. Derleme ve Çalıştırma

Paketler ROS 2 çalışma alanının `src` klasörüne yerleştirildikten sonra aşağıdaki komutlarla derlenir:

```bash
cd ~/ros2_ws
colcon build --packages-select alan_interfaces alan_py
source install/setup.bash
```

![Derleme ve arayüz kontrolü](ekran_goruntuleri/01_derleme_arayuz.png)

**Şekil 1.** Her iki paket başarıyla derlenmiş, servis arayüzü ve çalıştırılabilir düğümler kontrol edilmiştir.

Birinci terminalde sunucu çalıştırılır:

```bash
ros2 run alan_py server
```

İkinci terminalde istemci çalıştırılır:

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run alan_py client 5 4
```

![Sunucu ve istemci testi](ekran_goruntuleri/02_server_client.png)

**Şekil 2.** Sunucu ve istemci ayrı terminallerde çalıştırılmıştır. Tam sayı ve ondalıklı değerlerle yapılan testlerde alanın doğru hesaplandığı görülmektedir.

## 5. Servisin Doğrulanması

Sunucu çalışırken servis doğrudan terminal üzerinden çağrılmıştır:

```bash
ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: 6.0, height: 3.0}"
```

Servis çağrısının çıktısı:

```text
requester: making request: alan_interfaces.srv.RectangleArea_Request(width=6.0, height=3.0)

response:
alan_interfaces.srv.RectangleArea_Response(area=18.0, success=True)
```

![Servis doğrulama testi](ekran_goruntuleri/03_servis_testi.png)

**Şekil 3.** Servisin aktif olduğu ve doğru arayüzü kullandığı doğrulanmıştır. Doğrudan servis çağrısında alan 18.0 olarak hesaplanmıştır.

## 6. Negatif Değer Kontrolü (Bonus)

Genişlik veya yükseklik negatif olduğunda isteğin reddedilmesi ve `success` değerinin `False` olarak döndürülmesi sağlanmıştır.

![Negatif değer testi](ekran_goruntuleri/04_negatif_deger_testi.png)

**Şekil 4.** Negatif değerler hem istemci hem de doğrudan servis çağrısı üzerinden test edilmiştir. Geçersiz isteklerin reddedildiği görülmektedir.

## 7. Sonuç

Dikdörtgen alan hesaplama servisi başarıyla geliştirilmiş, sunucu ve istemci arasındaki iletişim doğrulanmıştır. Negatif değer kontrolü de başarıyla gerçekleştirilmiştir.
