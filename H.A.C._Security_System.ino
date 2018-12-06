



int microphone = 0;
int reed = 0;
int temp = 0;





void setup() {
  Serial.begin(115200);
  Serial1.begin(9600);

}

void loop() {
  microphone = analogRead(A3);
  reed = analogRead(A2);
  temp = analogRead(A1);

  Serial.println(reed);
  
  //Serial.println(microphone);
  //Serial1.write(120);
  
  if(microphone > 2500){
    //Serial.println("we've got a problem!");
    Serial1.write(120);     // corresponds to x
  }else{
    delay(2);
    Serial1.write(119);
  }
  if(reed > 1000){
    //Serial.println("we've got a problem!");
    Serial1.write(121);    // corresponds to y
  }else{
    delay(2);
    Serial1.write(119);
  }
  if(temp > 1300){
    //Serial.println("we've got a problem!");
    Serial1.write(122);   // corresponds to z
  }else{
    delay(2);
    Serial1.write(119);
  }
  
  
}
