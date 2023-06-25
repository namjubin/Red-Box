#define x A6
#define y A7
#define k 6
#define btn1 5
#define btn2 4
#define btn3 3
#define btn4 2

void setup() {
  Serial.begin(9600);

  pinMode(x, INPUT);
  pinMode(y, INPUT);
  pinMode(k, INPUT);
  pinMode(btn1, INPUT);
  pinMode(btn2, INPUT);
  pinMode(btn3, INPUT);
  pinMode(btn4, INPUT);
}

void loop() {
  Serial.print(analogRead(x));
  Serial.print(" ");
  Serial.print(analogRead(y));
  Serial.print(" ");
  Serial.print(digitalRead(k));
  Serial.print(" ");
  Serial.print(digitalRead(btn1));
  Serial.print(" ");
  Serial.print(digitalRead(btn2));
  Serial.print(" ");
  Serial.print(digitalRead(btn3));
  Serial.print(" ");
  Serial.println(digitalRead(btn4));
  delay(150);
}
