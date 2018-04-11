#include<Servo.h> //Servo 라이브러리를 추가
Servo servo1;
Servo servo2;//Servo 클래스로 servo객체 생성
int value = 0;    // 각도를 조절할 변수 value

void setup() {
  servo1.attach(7); 
  servo2.attach(6); //맴버함수인 attach : 핀 설정
  Serial.begin(9600); //시리얼 모니터 사용 고고
  servo1.write(value);
  servo2.write(value);
}

void loop() {
  if (Serial.available())
  {
    char in_data;
    in_data = Serial.read();
    if (in_data == '1'){
      value = 0;
      servo1.write(value);
    }
    else if(in_data == '2'){
      value = 90;
      servo1.write(value);           
    }   
    else if(in_data == '3'){
      value = 180;
      servo1.write(value);
    }
    else if(in_data == '4'){
      value = 0;
      servo2.write(value);
    }
    else if(in_data == '5'){
      value = 90;
      servo2.write(value);
    }
    else if(in_data == '6'){
      value = 180;
      servo2.write(value);
    }
  }
}
