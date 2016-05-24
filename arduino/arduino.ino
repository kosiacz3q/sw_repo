#include <Ethernet.h>
#include <SPI.h>

byte mac[] = { 0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x01 }; 
char server[] = "192.168.0.63";
IPAddress ip(192, 168, 0, 177); //if dhcp fail

EthernetClient client;

int sensor_id = 1;
int sensor = 6;
int sensor_value = 0;
String data;

void setup()
{
    pinMode(6, INPUT);
    pinMode(7, OUTPUT);
    Serial.begin(9600);

    if (Ethernet.begin(mac) == 0)
    {
        Serial.println("Failed to configure Ethernet using DHCP");
        Ethernet.begin(mac, ip);
    }

    delay(1000);
    Serial.println("Connecting in progress");
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

    if (client.connect(server,80))
    {

        client.print("POST /sensor/reading/");
        client.print(sensor_id);
        client.print("/");
        client.print(sensor_value)
        client.println("HTTP/1.1");

        client.println("Host: 192.168.0.63");

        client.println("Content-Type: application/x-www-form-urlencoded");

        client.print("Content-Length: ");
        client.println(0);
        client.println();
    }

    if (client.connected())
    {
        client.stop();
    }

    delay(3000);
}




