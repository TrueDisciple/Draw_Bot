




// MultiStepper steppers;




// void loop() {
//   // put your main code here, to run repeatedly:
//   // moveUp(5000);
//   // moveLeft(5000);

//   moveLinear(0,0);
//   // moveLinear(2000,2000);
//   moveLinear(2000,2000);
//   moveLinear(0,2000);

// }

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
