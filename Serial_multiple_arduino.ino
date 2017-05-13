int i=0;
void setup(){
Serial.begin(9600);
}
void loop()

{
Serial.print(i);
Serial.print(",10,");
Serial.print(i*2);
Serial.println(",");

delay(500);
i++;
}
