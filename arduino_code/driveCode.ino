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
// MultiStepper steppers;

void setup() {
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
  // put your main code here, to run repeatedly:
  // moveUp(5000);
  // moveLeft(5000);

  moveLinear(0,0);
  // moveLinear(2000,2000);
  moveLinear(2000,2000);
  moveLinear(0,2000);

}

void moveUp(int amount){
  stepperTop.move(amount);
  stepperBottom.move(amount);
  

  while(stepperTop.isRunning() || stepperBottom.isRunning()){
    stepperTop.run();
    stepperBottom.run();
  }
}

void moveDown(int amount){
  stepperTop.move(-amount);
  stepperBottom.move(-amount);
  stepperTop.run();
  stepperBottom.runSpeedToPosition();
}
void moveLeft(int amount){
  stepperLeft.move(amount);
  stepperRight.move(amount);
  
  while(stepperLeft.isRunning() || stepperRight.isRunning()){
    stepperLeft.run();
    stepperRight.run();
  }

}

void moveRight(int amount){
  stepperLeft.move(-amount);
  stepperRight.move(-amount);
  stepperLeft.run();
  stepperRight.runSpeedToPosition();
}

void moveLinear(int x, int y){
  stepperLeft.moveTo(x);
  stepperRight.moveTo(x);
  stepperTop.moveTo(y);
  stepperBottom.moveTo(y);

  while(stepperLeft.isRunning() || stepperRight.isRunning() || stepperTop.isRunning() || stepperBottom.isRunning()){
    stepperLeft.run();
    stepperRight.run();
    stepperTop.run();
    stepperBottom.run();
  }
}
