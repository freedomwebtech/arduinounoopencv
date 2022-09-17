

#include<Servo.h>
int servoPin = 3; 
Servo Servo1; 
void setup() {
  Servo1.attach(servoPin); 
  Serial.begin(9600);
 
}


void loop() {
  if (Serial.available() > 0)
  {
    int x_mid;
    if (Serial.read() == 'X')
    {
      x_mid = Serial.parseInt();  // read center x-coordinate
      Servo1.write(x_mid); 
    }
   

    // used for testing
   
    //Serial.println(x_mid);
  
  }
}
