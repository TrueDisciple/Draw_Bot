
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print(data);
    // if (data == "END") {
    //   Serial.print("KILL");
    // }
    // else {
    //   Serial.print(data);
    //   Serial.println();
    // }
    
    int string_count = 0;
    String data_parts[10];
    



  //   while (data.length() > 0)
  // {
  //   if (data == "END") {
  //     Serial.println("KILL");
  //     break;
  //   }
  //   // Serial.println("in the while loop");
  //   int index = data.indexOf(' ');
  //   if (index == -1) // No space found
  //   {
  //     data_parts[string_count++] = data;
  //     break;
  //   }
  //   else
  //   {
  //     data_parts[string_count++] = data.substring(0, index);
  //     data = data.substring(index+1);
  //   }
  // }
  //   for (int i = 0; i < string_count; i++)
  // {
  //   Serial.println(data_parts[i]);
  // }
    
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

