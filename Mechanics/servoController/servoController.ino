#include <Wire.h>

#define SLAVE_ADDRESS 0x08 // Arduino I2C slave address
#define ARRAY_SIZE 5       // Size of the array to receive

int receivedData[ARRAY_SIZE]; // Array to store received data

void setup() {
  Wire.begin(SLAVE_ADDRESS); // Initialize I2C communication as a slave
  Wire.onReceive(receiveEvent); // Call receiveEvent() function when receiving data
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  delay(100);
}

void receiveEvent(int numBytes) {
  int i = 0;
  while (Wire.available() && i < ARRAY_SIZE) {
    receivedData[i] = Wire.read(); // Read the incoming data byte into the array
    i++;
  }
  
  // Print received array
  Serial.print("Received Array: ");
  for (int j = 0; j < ARRAY_SIZE; j++) {
    Serial.print(receivedData[j]);
    Serial.print(" ");
  }
  Serial.println();
}
