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
        Serial.begin(115200);
}

// the loop routine runs over and over again forever:
void loop() 
{
        if(Serial.read()=='K')
        {
              int V0 = analogRead(A0);
              Serial.print(V0);
              Serial.print(" ");

              int V1 = analogRead(A1);
              Serial.print(V1);
              Serial.print(" ");

              int V2 = analogRead(A2);
              Serial.print(V2);
              Serial.print(" ");

              int V3 = analogRead(A3);
              Serial.print(V3);
              Serial.print(" ");

              int V4 = analogRead(A4);
              Serial.print(V4);
              Serial.print(" ");

              int V5 = analogRead(A5);
              Serial.print(V5);
              Serial.print(" ");
        } 
}
