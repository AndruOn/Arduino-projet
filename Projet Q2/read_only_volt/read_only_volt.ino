/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/
int count = 0;

// the setup routine runs once when you press reset:
void setup() {
  // on démarre la liaison
  // en la réglant à une vitesse de 9600 bits par seconde.
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() 
{
        // read the input on analog pin 0:
        
        // print out the value you read:
        
        int V = map(analogRead(A0),0,1023,0,5000);
        Serial.print(V);
        count++;
        Serial.print(" ");
        delay(50);        // delay in between reads for stability
        
}
