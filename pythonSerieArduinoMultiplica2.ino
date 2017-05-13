char g=' ';
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600); 
}
// the loop routine runs over and over again forever:
void loop() {
  while(Serial.available()>0)
  {
    g=Serial.read();
    if(g=='N')
    {
      long num1=Serial.parseInt();
      long num2=Serial.parseInt();
      long num3= num1*num2;
      Serial.println(num3);
    }
    // delay in between reads for stability
  }
}





