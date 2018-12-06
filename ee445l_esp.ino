#include <Wire.h>
#include <ESP8266WiFi.h>
#include <WiFiUDP.h>

const char* ssid     = "MySpectrumWiFi60-2G";
const char* password = "betterocean560";
const char* ip = "192.168.1.15";


//const char* ssid     = "EE-IOT-Platform-03";
//const char* password = "dUQQE?&W44x7";
//const char* ip = "10.145.231.183";



WiFiUDP Client;

int sum = 0;
char microphone_trigger, reed_trigger, temperature_trigger;

void setup() {
  pinMode(2, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
  digitalWrite(2, HIGH);
  Serial.begin(9600);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println(".....");
  }
 
  Serial.println("i'm connected");
  
  digitalWrite(2, LOW);
  delay(500);
  digitalWrite(2, HIGH);
  delay(500);
  digitalWrite(2, LOW);
  
  Serial.flush();
}

// the loop function runs over and over again forever
void loop() {
  
  while (Serial.available() > 0)   {



      microphone_trigger = Serial.read();  // assigns one byte (as serial.read()'s only input one byte at a time
      //Serial.println(microphone_trigger);
      if( microphone_trigger == 'x'){
        sum += 1;              
      }

      reed_trigger = Serial.read();  // assigns one byte (as serial.read()'s only input one byte at a time
      //Serial.println(reed_trigger);
      if( reed_trigger == 'y'){
        sum += 10;
      }

      temperature_trigger = Serial.read();  // assigns one byte (as serial.read()'s only input one byte at a time
      //Serial.println(temperature_trigger);
      if( temperature_trigger == 'z'){
        sum += 100;
      }

      Client.beginPacket(ip,6789);
      Client.write(sum);
      Client.endPacket();
      delay(2);
      
      sum = 0;
      yield();
  } 

  yield();
  
 
}
