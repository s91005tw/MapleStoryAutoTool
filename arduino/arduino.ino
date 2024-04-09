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
const int localUdpPort = 80;

WiFiServer wifiServer(localUdpPort);

// IPAddress local_IP(192,168,100,6);
// IPAddress gateway(192,168,100,1);
// IPAddress subnet(255,255,255,0);

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.print("Connecting to ");  // 連上你所指定的Wi-Fi，並在序列埠螢幕中，印出 ESP32 web server 的 IP address
  Serial.println(ssid);

  // WiFi.config(local_IP,gateway,subnet);
  // WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  int WifiTryCount=0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    if (WifiTryCount++ >= 20)  ESP.restart();
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
        c = client.readStringUntil('0');
        Serial.println(c + (int) c[0]);
        Serial.println((int) c[0]);
        if(c[0] =='H'){//UP
          Serial.println("UP");
          bleKeyboard.press(KEY_UP_ARROW);
        }
        if(c[0] =='P'){//DOWN
          Serial.println("DOWN");
          bleKeyboard.press(KEY_DOWN_ARROW);
        }
        if(c[0] =='K'){//LEFT
          Serial.println("LEFT");
          bleKeyboard.press(KEY_LEFT_ARROW);
        }
        if(c[0] =='M'){//RIGHT
          Serial.println("RIGHT");
          bleKeyboard.press(KEY_RIGHT_ARROW);
        }

        if(c[0] =='*'){//shift
          Serial.println("shift");
          bleKeyboard.press(KEY_LEFT_SHIFT);
        }
        if((int)c[0] == 29){//alt
          Serial.println("ctrl");
          bleKeyboard.press(KEY_LEFT_CTRL);
        }
        if(c[0] =='8'){//alt
          Serial.println("alt");
          bleKeyboard.press(KEY_LEFT_ALT);
        }
        // if(c[0] =='9'){//space
        //   Serial.println("space");
        //   bleKeyboard.press(KEY_UP_ARROW);
        // }

        if((int)c[0] == 73){//pageup
          Serial.println("pageup");
          bleKeyboard.press(KEY_PAGE_UP);
        }
        if((int)c[0] == 81){//pagedown
          Serial.println("pagedown");
          bleKeyboard.press(KEY_PAGE_DOWN);
        }
        if((int)c[0] == 71){//home
          Serial.println("home");
          bleKeyboard.press(KEY_HOME);
        }
        if((int)c[0] == 79){//end
          Serial.println("end");
          bleKeyboard.press(KEY_END);
        }

        if((int)c[0] == 28){//enter
          Serial.println("enter");
          bleKeyboard.press(KEY_RETURN);
        }
        if((int)c[0] == 1){//esc
          Serial.println("esc");
          bleKeyboard.press(KEY_ESC);
        }

        Serial.println();
        delay(100);
        bleKeyboard.releaseAll();//release
      }

    }
  }

}