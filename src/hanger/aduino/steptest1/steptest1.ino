#include <Stepper.h>
 
int in1Pin = 12;
int in2Pin = 11;
int in3Pin = 10;
int in4Pin = 9;
 
Stepper motor(768, in1Pin, in2Pin, in3Pin, in4Pin); 
 
void setup()
{
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
  if (Serial.available())
  {
    int steps = Serial.parseInt();
    motor.step(steps);
  }
}
