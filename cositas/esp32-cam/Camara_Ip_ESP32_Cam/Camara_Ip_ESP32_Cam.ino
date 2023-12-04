/*  
  Desarrollado por Edison Sasig | Roboticoss
  Aprende en mi sitio web: https://roboticoss.com/cursos/
  
  Cargar con Arduino nano: Cuando este en ...... presionar el boton reset
  Instalacion de Arduino-ESP32 la https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/installing.html
  Libreria IP CAM: https://github.com/yoursunny/esp32cam
 
 */

#include "WifiCam.hpp"
#include <WiFi.h>

static const char* WIFI_SSID = "A777";
static const char* WIFI_PASS = "98761234";

esp32cam::Resolution initialResolution;

WebServer server(80);

void
setup()
{
  Serial.begin(115200);
  Serial.println();
  delay(2000);

  WiFi.persistent(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  if (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("WiFi failure");
    delay(5000);
    ESP.restart();
  }
  Serial.println("WiFi connected");

  {
    using namespace esp32cam;

    initialResolution = Resolution::find(1024, 768);

    Config cfg;
    cfg.setPins(pins::AiThinker);
    cfg.setResolution(initialResolution);
    cfg.setJpeg(80);

    bool ok = Camera.begin(cfg);
    if (!ok) {
      Serial.println("camera initialize failure");
      delay(5000);
      ESP.restart();
    }
    Serial.println("camera initialize success");
  }

  Serial.println("camera starting");
  Serial.print("http://");
  Serial.println(WiFi.localIP());

  addRequestHandlers();
  server.begin();
}

void
loop()
{
  server.handleClient();
}
