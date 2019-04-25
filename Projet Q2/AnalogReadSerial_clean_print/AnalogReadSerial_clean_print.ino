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
    int sensorValue = analogRead(A0);
    do
    {
        if(count < 1000)
        {
          // read the input on analog pin 0:
          int sensorValue = analogRead(A0);
          // print out the value you read:
          
          Serial.print("A0volt: ");
          int V = map(sensorValue,0,1023,0,5000)/1000;
          Serial.print(V);
          Serial.print(",");
          Serial.print(map(sensorValue,0,1023,0,5000)- V*1000);
          count++;
          Serial.print("   testn°: ");
          Serial.print(count);
          Serial.println(" ");
          delay(1);        // delay in between reads for stability
        }
    }while(sensorValue < 1023);
}
