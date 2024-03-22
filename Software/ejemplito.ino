int n,n1,n2;
int sw1, sw2, sw3;

void setup() {
  // put your setup code here, to run once:
  DDRD = 0xFF;// todos los bits son salida :)
  DDRB = 0x00;// PB0, PB1, PB2 son entradas --> sw
  DDRC = 0x00;// es donde pondrás los numeros y los leerás
}

void loop() {
  // put your main code here, to run repeatedly:
     // la cuenta va a aparecer en ek led tons need salida!
  sw1 = PINB&0x01;
  if (sw1 == 0x01){
    sw1 = PINB&0x01;
    while(sw1 == 0x01)
      {sw1 = PINB&0x01;}
    n1=PINC --> como es variable si aplastas, cuando es estado NO
  }
  sw2 = PINB&0x02;
  if (sw2 == 0x02){
    sw2 = PINB&0x02;
    while(sw2 == 0x02)
      {sw2 = PINB&0x02;}
    n2=PINC
  }

  sw3 = PINB&0b00000100;//0x04
  if (sw3 == 0x04){
    sw3 = PINB&0x04;
    while(sw3 == 0x04)
      {sw3 = PINB&0x04;}
    n=n1+n2
    PORTD = n;
  }
  
 
}