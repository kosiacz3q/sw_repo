#include <Ethernet.h>
#include <SPI.h>

byte mac[] = { 0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x01 }; 
char server[] = "server_address";
IPAddress ip(192, 168, 0, 177); //if dhcp fail

EthernetClient client;

int sensor = 6;
int sensor_value = 0;
String data;

void setup() { 
    pinMode(6, INPUT);
    pinMode(7, OUTPUT);
	Serial.begin(9600);

	if (Ethernet.begin(mac) == 0) {
		Serial.println("Failed to configure Ethernet using DHCP"); 
		Ethernet.begin(mac, ip);
	}
	
	delay(1000);
	Serial.println("Connecting in progress");
	
	data = "";
}

void loop(){

        digitalRead(sensor);
        sensor_value=digitalRead(sensor);
 
        Serial.println(sensor_value);
 
        if (digitalRead(sensor)==1)
           {
             digitalWrite(7, HIGH);
           }
 
        else 
           {
             digitalWrite(7, LOW);
           }       

  if(sensor_value>0){
	if (client.connect(server,80)) {
		client.println("POST /motion/reading/ HTTP/1.1"); 
		client.println("Host: xxx.xxx.xxx"); // SERVER ADDRESS HERE TOO
		client.println("Content-Type: application/x-www-form-urlencoded"); 
		client.print("Content-Length: "); 
		client.println(data.length()); 
		client.println(); 
		client.print(data); 
	} 

	if (client.connected()) { 
		client.stop();
	}

	delay(3000);
}
else{
Serial.println("No data to send");
delay(300);
}

}




