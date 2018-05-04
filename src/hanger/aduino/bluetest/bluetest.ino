#include <SoftwareSerial.h>
#include<Servo.h> //Servo 라이브러리를 추가
Servo servo1;
int bluetoothTx = 2;
int bluetoothRx = 3;
int value = 0;
SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);
 
void setup()
{
  servo1.attach(7);
  Serial.begin(9600);//시리얼 통신 초기화
  bluetooth.begin(9600);//블루투스 통신 초기화
  servo1.write(value);
}
 
 
void loop()
{ 
  //블루투스에서 읽은 문자를 시리얼로 전송
  if(bluetooth.available())
  {
    char toSend = (char)bluetooth.read();
    Serial.print(toSend);
    if (toSend == '1'){
      value = 0;
      servo1.write(value);
    }
    else if(toSend == '2'){
      value = 90;
      servo1.write(value);           
    }   
    else if(toSend == '3'){
      value = 180;
      servo1.write(value);
    }
  }
 
  //시리얼로에서 읽은 문자를 블루투스로 전송
  if(Serial.available())
  {
    char toSend = (char)Serial.read();
    bluetooth.print(toSend);
  }
}
