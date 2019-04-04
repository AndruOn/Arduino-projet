
int carlu;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
    // put your main code here, to run repeatedly:
    if(Serial.available() > 0)
    {
        carlu= Serial.read();
        if(carlu >= 'a' && carlu <='z')
        {
            carlu = carlu - 'a'; // on garde juste le "numéro de lettre"
            carlu = carlu + 'A'; // on passe en majuscule
        }
        else if(carlu >='A' && carlu <='Z')
        {
            carlu = carlu - 'A'; // on garde juste le "numéro de lettre"
            carlu = carlu + 'a'; // on passe en minuscule
        }
        Serial.write(carlu);
    }
}
