/*********
  這個程式，原始創作，來自：
  Rui Santos
  Complete project details at http://randomnerdtutorials.com
*********/

// 匯入 Arduino WiFi.h  library 程式庫，用 Arduino 語言，開設一個網路伺服器 web server
#include <WiFi.h>
#include <BleKeyboard.h>
#include <WiFiUdp.h>

BleKeyboard bleKeyboard;//宣告一個藍芽鍵盤

const char* ssid = "JIANG";       // 雙引號內，修改為你要 ESP32 連上的 WiFi 網路名稱 SSID
const char* password = "0910455818";   // 雙引號內，鍵入此網路的密碼
const int localUdpPort = 8088;

WiFiServer wifiServer(localUdpPort);

IPAddress local_IP(192,168,100,6);
IPAddress gateway(192,168,100,1);
IPAddress subnet(255,255,255,0);

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  Serial.print("Connecting to ");  // 連上你所指定的Wi-Fi，並在序列埠螢幕中，印出 ESP32 web server 的 IP address
  Serial.println(ssid);

  WiFi.config(local_IP,gateway,subnet);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  udp.begin(localUdpPort);          // 啟動 UDP
  Serial.printf("Listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUdpPort);

  Serial.println("BLE鍵盤準備連線");
  bleKeyboard.setName("小霸王BLEKeyBoard"); //自行設定藍芽鍵盤名稱
  bleKeyboard.begin();

  wifiServer.begin();
}

void loop(){
  WiFiClient client = wifiServer.available();
  String c;
  if (client) {
    while (client.connected()) {
      while (client.available()>0) {
        c = client.readString();
        Serial.println(c);
        Serial.println();
        
        if(c = 'q'){
          Serial.println("c = 'q'");
        }
        if(c = 'esc'){
          Serial.println("c = 'esc'");
        }
        if(c = 'alt'){
          Serial.println("c = 'alt'");
        }
        if(c = 'ctrl'){
          Serial.println("c = 'ctrl'");
        }
        if(c = 'spcae'){
          Serial.println("c = 'space'");
        }
        if(c = 'shift'){
          Serial.println("c = 'shift'");
        }
      }
    delay(50);
    }
  }

//   int packetSize = udp.parsePacket();
//   if (packetSize) {
//        char incomingPacket[255];
//        int len = udp.read(incomingPacket, 255);
//        if (len > 0) {
//           incomingPacket[len] = 0;
//        }

//        Serial.printf("Received packet: %s\n", incomingPacket);

//        udp.beginPacket(udp.remoteIP(), udp.remotePort());
//        udp.write((uint8_t*)"ACK", strlen("ACK")); // 回傳 ACK
//        udp.endPacket();
//  }
}