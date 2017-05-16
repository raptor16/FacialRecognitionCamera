include <Servo.h>

Servo servoX;
Servo servoY;

int incoming[2];

void setup() {
  Serial.begin(9600);
  servoX.attach(3);
  servoY.attach(6);
}

void loop() {
  while (Serial.available() >=2){
    for (int i=0; i<2; i++){
      incoming[i] = Serial.read();
      servoX.write(incoming[0]);
      servoY.write(incoming[1]);}
      }
}
