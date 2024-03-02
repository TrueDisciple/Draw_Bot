
const int SPEED = 400;
const int ACCEL = 100;
#include <AccelStepper.h>


AccelStepper stepperPen(AccelStepper::DRIVER, 2, 5);

void setup() {
  // put your setup code here, to run once:
  stepperPen.setMaxSpeed(SPEED);
  stepperPen.setAcceleration(ACCEL);
}

void loop() {
  // put your main code here, to run repeatedly:
  penUp();
  delay(1000);
  penDown();
  
}
void movePen(int pos){
  stepperPen.moveTo(pos);
  

  while(stepperPen.isRunning()){
    stepperPen.run();
  }
}

void penUp(){
  stepperPen.moveTo(0);
  

  while(stepperPen.isRunning()){
    stepperPen.run();
  }
}
void penDown(){
  stepperPen.moveTo(300);
  

  while(stepperPen.isRunning()){
    stepperPen.run();
  }
}