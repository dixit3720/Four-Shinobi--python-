#include <Wire.h>

int ADXL345 = 0x53;
float X, Y, Z;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin();

  Wire.beginTransmission(ADXL345);
  Wire.write(0x2D);

  Wire.write(8);
  Wire.endTransmission();
  delay(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  Wire.beginTransmission(ADXL345);
  Wire.write(0x32);
  Wire.endTransmission(false);
  Wire.requestFrom(ADXL345, 6, true);
  
  X = (Wire.read() | Wire.read() << 8);
  Y = (Wire.read() | Wire.read() << 8);
  Z = (Wire.read() | Wire.read() << 8);
  X=(X/230)*9.8;
  Y=(Y/256)*9.8;
  Z=(Z/282)*9.8;
  float ac=sqrt((X*X)+(Y*Y)+(Z*Z));
  //Serial.println(ac);
  
  Serial.println(X);
  // Serial.print("------- ");
  Serial.println(Y);
  // Serial.print("******** ");
  Serial.println(Z);
  // Serial.println("######## ");
  delay(200);
    
  
  

}

