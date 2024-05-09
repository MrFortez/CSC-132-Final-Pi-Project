#include <Wire.h>
#include <Servo.h>
#include <string.h>

Servo pinionServo;
Servo elbowServo;
// Servo wristServo;

float cutDistance = 1;
float foodSize = 12;
int numOfCuts = 5;

void setup() {
  pinionServo.attach(4);
  elbowServo.attach(6);
  // wristServo.attach(8);
  Serial.begin(9600);
  // moveRack(0);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming string until newline character ('\n') is received
    String receivedString = Serial.readString();

    // Split the string by spaces and convert each substring to a float
    char *ptr = strtok((char *)receivedString.c_str(), " ");
    if (ptr != NULL) {
      cutDistance = atof(ptr);
      ptr = strtok(NULL, " ");
      if (ptr != NULL) {
        foodSize = atof(ptr);
        ptr = strtok(NULL, " ");
        if (ptr != NULL) {
          numOfCuts = atof(ptr);
        }
      }
    }

    // if (receivedString == "2 2 2") {
    //   moveRack(180);      
    // }
    // else if (receivedString != "") {
    //   moveRack(90);
    // }
    // fullCutSequence();
    // delay(2000);
  }
  // cutDistance = 2;
  // numOfCuts = 4;
  // fullCutSequence();
  // pinionServo.write(0);
  halfIncrementServo(pinionServo);
}

// 5 to 16
void moveWrist(int angle) {
  // double newAngle = angle;
  // if (newAngle > 16) {
  //   newAngle = 16;
  // }
  // if (newAngle < 5) {
  //   newAngle = 5;
  // }

  // wristServo.write(newAngle);
  // Serial.println(wristServo.read());
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

  servoSlowMove(newAngle, pinionServo);
  Serial.println(pinionServo.read());
}

// Used For Pinion Testing
void halfIncrementServo(Servo servo) {
  if (servo.read() >= 90) {
    Serial.print("bruh");
    servoSlowMove(0, servo);
  }
  else{
    servoSlowMove(servo.read() + 10, servo);
  }
}

// Moves a servo slowly by incrementing it by 1 every 50 milliseconds
void servoSlowMove(int angle, Servo servo) {
  if (servo.read() > angle) {
    for (int i = servo.read(); servo.read() != angle; i -= 3) {
      servo.write(i);
      delay(10);
      Serial.println(i);
    }
  }
  else {
    for (int i = servo.read(); servo.read() != angle; i += 3) {
      servo.write(i);
      delay(50);
      Serial.print(i);
    }

  }
}

// Slicing motion for the arm
void servoSlice() {
  moveElbow(70);
  delay(1000);
  moveElbow(115);
  delay(1000);
}

void fullCutSequence() {
  // Convert from inches to pinion servo angle (16 degrees on the Pinion servo moves it 1 inch)
  int cutServoAngle = cutDistance * 16;
  Serial.print(cutServoAngle);

  // do however many cuts the user inputed
  for (int i = 0; i < numOfCuts; i++) {
    Serial.print("ok booker");
    // Move the rack by however wide the cuts should be
    moveRack(pinionServo.read() + cutServoAngle);
    delay(1000);
    servoSlice();
  }

  // Rezero the Pinion
  moveRack(0);
}
