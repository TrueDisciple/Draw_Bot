const int StepX = 2;
const int DirX = 5;
const int StepY = 3;
const int DirY = 6;
const int StepZ = 4;
const int DirZ = 7;
const int StepA = 12;
const int DirA = 13;
const int SPEED = 10000;
const int ACCEL = 10000;

#include <AccelStepper.h>
#include <MultiStepper.h>

AccelStepper stepperLeft(AccelStepper::DRIVER, 2, 5);
AccelStepper stepperRight(AccelStepper::DRIVER, 12, 13);
AccelStepper stepperTop(AccelStepper::DRIVER, 3, 6);
AccelStepper stepperBottom(AccelStepper::DRIVER, 4, 7);

void setup() {
  Serial.begin(9600);
  stepperLeft.setMaxSpeed(SPEED);
  stepperLeft.setAcceleration(ACCEL);
  stepperRight.setMaxSpeed(SPEED);
  stepperRight.setAcceleration(ACCEL);
  stepperTop.setMaxSpeed(SPEED);
  stepperTop.setAcceleration(ACCEL);
  stepperBottom.setMaxSpeed(SPEED);
  stepperBottom.setAcceleration(ACCEL);


  stepperRight.setPinsInverted(true,false,false);
  stepperBottom.setPinsInverted(true,false,false);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    Serial.print(data);   
    int string_count = 0;
    String data_parts[5];
    


// this while loop methodically splits up the data string by spaces adding data in parts to data_parts
// ##########################################################
    while (data.length() > 0) {

    // if (data == "END") {
    //   Serial.println("KILL");
    //   break;
    // }
    int index = data.indexOf(' ');
    if (index == -1) // No space found
    {
      data_parts[string_count++] = data;
      break;
    }
    else
    {
      data_parts[string_count++] = data.substring(0, index);
      data = data.substring(index+1);
    }
  }
  // #########################################################
   if (false) { // will have circle logic here 
      return;
      // TODO add circular line drawing
   }
   else {
    // Serial.println("in else");
    Serial.print(data_parts[1].toInt());
    Serial.println(data_parts[2].toInt());
    moveLinear(data_parts[1].toInt(), data_parts[2].toInt());
   }
    
  }
}

bool isCircle (String data) {
  if (data.substring(data.indexOf(" ") == "CIRCLE")) {
    return true;
  }
  else {
    return false;
  }
}



