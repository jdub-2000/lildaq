#include <dht.h>

dht DHT;

#define DHT11_PIN 7

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int chk = DHT.read11(DHT11_PIN);

  Serial.print(DHT.humidity);
  Serial.print(",");
  Serial.println(((DHT.temperature)*1.8)+32);
  delay(10000);

}
