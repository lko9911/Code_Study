// CAN 통신 예제 코드

#include <SPI.h>
#include "mcp_can.h"

const int SPI_CS_PIN = 10;
MCP_CAN CAN(SPI_CS_PIN);

void setup() {
  Serial.begin(115200);

  if (CAN.begin(MCP_ANY, CAN_500KBPS, MCP_8MHZ) == CAN_OK) {
    Serial.println("CAN Init OK");
  } else {
    Serial.println("CAN Init Fail");
    while (1);
  }

  CAN.setMode(MCP_NORMAL);
}

void loop() {
  if (!digitalRead(2)) {  // INT 핀 확인
    long unsigned int rxId;
    unsigned char len = 0;
    unsigned char rxBuf[8];

    CAN.readMsgBuf(&rxId, &len, rxBuf);

    Serial.print("ID: 0x");
    Serial.print(rxId, HEX);
    Serial.print(" | Data: ");

    for (int i = 0; i < len; i++) {
      Serial.print(rxBuf[i], HEX);
      Serial.print(" ");
    }
    Serial.println();
  }
}
