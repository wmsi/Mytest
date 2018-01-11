//Serial printer for the EMG sensor
//This code is for printing the EMG value on the
//serial monitor.
//
//© Au Robots 8.4.2017

int count = 0;
String sensor1 = " ";
String sensor2 = " ";

void setup() {
  Serial.begin(9600);
}

void loop() {

  //Takes in the first entry and assigns to sensor 1
  while (count == 0){
    Serial.println("Please type first attachment site");
    while (!Serial.available()); //Wait for user to send a character
    sensor1 = String(Serial.readString());
    count++;
  }
  //Takes in the second entry and assigns to sensor 2
  while (count == 1){
    Serial.println(F("Please type second attachment site"));
    while (!Serial.available()); //Wait for user to send a character
    sensor2 = String(Serial.readString());
    count++;
  }
  //Takes in the next entry to begin reading from sensors
  while (count == 2){
     Serial.println(F("Press a key to read user data"));
     while (!Serial.available()); //Wait for user to send a character
     Serial.read(); //Throw away the user's character
     count++;
  }

  //Uses analog readings and determines if flexing
  int rval = analogRead(2);
  int lval = analogRead(1);
  
  bool r = rightSensor(rval);
  bool l = leftSensor(lval);
  
  if(r and not(l)){
    Serial.println(sensor1);
  }
  else if (l and not(r)){
    Serial.println(sensor2);
  }
  else if(r and l){
    Serial.println("both");
  }
  else 
    Serial.println("none");
  
  delay(1000);
}

//Checks if the right sensor is activated above threshold
bool rightSensor(int r_val)
{
  if (r_val > 400){
    return true;
  }
  return false;
}

//Checks if the left sensor is activated above threshold
bool leftSensor(int l_val)
{
  if (l_val > 400){
    return true;
  }
  return false;
}

