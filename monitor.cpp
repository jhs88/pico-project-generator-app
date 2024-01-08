#include <Arduino.h>

const char ADDR[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
const char DATA[] = {16, 17, 18, 19, 20, 21, 22, 26};
#define CLOCK_MONITOR 27 // montior clock
#define READ_WRITE 28    // monitor read/write

void setup()
{
    for (int n = 0; n < 16; n += 1)
    {
        pinMode(ADDR[n], INPUT);
    }
    for (int n = 0; n < 8; n += 1)
    {
        pinMode(DATA[n], INPUT);
    }
    pinMode(CLOCK_MONITOR, INPUT);
    pinMode(READ_WRITE, INPUT);

    attachInterrupt(digitalPinToInterrupt(CLOCK_MONITOR), onClock, RISING);

    Serial.begin(57600);
}

void onClock()
{
    char output[15];

    unsigned int address = 0;
    for (int n = 0; n < 16; n += 1)
    {
        int bit = digitalRead(ADDR[n]) ? 1 : 0;
        Serial.print(bit);
        address = (address << 1) + bit;
    }

    Serial.print("   ");

    unsigned int data = 0;
    for (int n = 0; n < 8; n += 1)
    {
        int bit = digitalRead(DATA[n]) ? 1 : 0;
        Serial.print(bit);
        data = (data << 1) + bit;
    }

    sprintf(output, "   %04x  %c %02x", address, digitalRead(READ_WRITE) ? 'r' : 'W', data);
    Serial.println(output);
}

void loop()
{
}