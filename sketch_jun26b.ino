int val = 0; //入力される値を格納する為の変数
void setup() {
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
  //ANALOG INの０番ピンからデータを受け取る
  val=analogRead(0);
  delay(100);
}

