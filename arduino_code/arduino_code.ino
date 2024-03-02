
// globals
char current_data[] = {};

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    // Serial.println("data recieved!");
    
    int string_count = 0;
    String data_parts[10];

    while (data.length() > 0)
  {
    // Serial.println("in the while loop");
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
    for (int i = 0; i < string_count; i++)
  {
    // Serial.print(i);
    // Serial.print(" ");
    Serial.println(data_parts[i]);
  }

    // Serial.print("Hello from Gondor!");
    // Serial.println(data); 
    
  }
}

// meaningfully splits the data from the string sent over serial and updates the global array of string objects  
bool isCircle (String data) {
  if (data.substring(data.indexOf(" ") == "Circle")) {
    return true;
  }
  else {
    return false;
  }
}

