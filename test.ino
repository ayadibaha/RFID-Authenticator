void setup() {
	Serial.begin(9600);
	Serial.println("Ready");
}
void loop() {
	if(Serial.available()){
		Serial.println("Im ready to work");
	}
	delay(100);
}
