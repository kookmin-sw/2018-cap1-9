#include <SoftwareSerial.h>
#include<Servo.h> //Servo 라이브러리를 추가
#include <Stepper.h>

Servo servo1;
Servo servo2;
Servo servo3;
int in1Pin = 12;
int in2Pin = 11;
int in3Pin = 10;
int in4Pin = 9;
int in5Pin = 8;
int in6Pin = 7;
int in7Pin = 6;
int bluetoothTx = 2;
int bluetoothRx = 1;
int value = 0;
int value1 = 0;
int value2 = 0;
Stepper motor(768, in1Pin, in2Pin, in3Pin, in4Pin); 
SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);
 
void setup()
{
  servo1.attach(in5Pin);
  servo2.attach(in6Pin);
  servo3.attach(in7Pin);
  Serial.begin(9600);//시리얼 통신 초기화
  bluetooth.begin(9600);//블루투스 통신 초기화
  servo1.write(value);
  servo2.write(value);
  servo3.write(value);

  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  while (!Serial);

  Serial.begin(9600);
  motor.setSpeed(20);
}
 
 
void loop()
{ 
  //블루투스에서 읽은 문자를 시리얼로 전송
  if(bluetooth.available())
  {
    char toSend = (char)bluetooth.read();
    Serial.print(toSend);
    if (toSend == '1' || toSend == '2' || toSend == '3'){
      value1 = 0;
      motor.step(value1);
      if(toSend == '1')
      {
        value2 = 0;
        servo1.write(value2);  
      }
      else if(toSend == '2')
      {
        value2 = 90;
        servo1.write(value2);  
      }
      else if(toSend == '3')
      {
        value2 = 180;
        servo1.write(value2);  
      }
    }
    else if(toSend == '4' || toSend == '5' || toSend == '6'){
      value1 = 166;
      motor.step(value1);
      if(toSend == '4')
      {
        value2 = 0;
        servo2.write(value2);  
      }
      else if(toSend == '5')
      {
        value2 = 90;
        servo2.write(value2);  
      }
      else if(toSend == '6')
      {
        value2 = 180;
        servo2.write(value2);  
      }
    }
    else if(toSend == '7' || toSend == '8' || toSend == '9'){
      value1 = 166;
      motor.step(value1);
      if(toSend == '7')
      {
        value2 = 0;
        servo3.write(value2);  
      }
      else if(toSend == '8')
      {
        value2 = 90;
        servo3.write(value2);  
      }
      else if(toSend == '9')
      {
        value2 = 180;
        servo3.write(value2);  
      }
    }
  }
 
  //시리얼로에서 읽은 문자를 블루투스로 전송
  if(Serial.available())
  {
    char toSend = (char)Serial.read();
    bluetooth.print(toSend);
  }
}
