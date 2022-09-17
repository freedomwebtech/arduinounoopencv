#include <Servo.h>
Servo Servo1; 
int servoPin = 3; 
void setup() {
  Servo1.attach(servoPin); 
  Serial.begin(9600);
 
}


void loop(){
  
    int x;
    if (Serial.read() == 'C')
    {
      x = Serial.parseInt();  // read center x-coordinate
      Servo1.write(x); 
    }
   

    // used for testing
   
    Serial.println(x);
  
  
}
