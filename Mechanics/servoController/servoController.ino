#include <Wire.h>
#include <Servo.h>

#define SLAVE_ADDRESS 0x08

Servo pinionServo;
Servo elbowServo;
Servo wristServo;


void setup() {
  // Initialize I2C communication as a slave with address SLAVE_ADDRESS
  Wire.begin(SLAVE_ADDRESS);
  
  // Define a callback function to handle incoming data
  Wire.onReceive(receiveData);
  
  pinionServo.attach(4);
  elbowServo.attach(6);
  wristServo.attach(8);
  Serial.begin(9600);
}

void loop() {
  delay(100);
  // Serial.println(wristServo.read());
  moveRack(0);
  // moveWrist(5);
  // elbowServo.write(90);
  delay(10000);
  // elbowServo.write(125);
  // moveWrist(16);
  moveRack(180);
  delay(10000);
}

void receiveData(int byteCount) {
  Serial.print("poggers");
  while (Wire.available()) {
    // Read incoming byte from master
    int receivedByte = Wire.read();
    
    // Print received byte to serial monitor
    Serial.print("Received byte from master: ");
    Serial.println(receivedByte);
  }
}

// 5 to 16
void moveWrist(int angle) {
  double newAngle = angle;
  if (newAngle > 16) {
    newAngle = 16;
  }
  if (newAngle < 5) {
    newAngle = 5;
  }

  wristServo.write(newAngle);
  Serial.println(wristServo.read());
}

// 65 to 165
void moveElbow(int angle) {
  double newAngle = angle;
  if (newAngle > 165) {
    newAngle = 165;
  }
  if (newAngle < 65) {
    newAngle = 65;
  }

  elbowServo.write(newAngle);
  Serial.println(elbowServo.read());
}


// 0 to 180
void moveRack(int angle) {
  double newAngle = angle;
  if (newAngle > 180) {
    newAngle = 180;
  }
  if (newAngle < 0) {
    newAngle = 0;
  }

  pinionServo.write(newAngle);
  Serial.println(pinionServo.read());
}
