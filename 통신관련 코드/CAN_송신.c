// 송신코드 예제

#include <SPI.h>
#include "mcp_can.h"

const int SPI_CS_PIN = 10;
MCP_CAN CAN(SPI_CS_PIN);

void setup() {
  Serial.begin(115200);

  // CAN 초기화
  if (CAN.begin(MCP_ANY, CAN_500KBPS, MCP_8MHZ) == CAN_OK) {
    Serial.println("CAN Init OK");
  } else {
    Serial.println("CAN Init Fail");
    while (1);
  }

  CAN.setMode(MCP_NORMAL);  // 정상 모드
}

void loop() {
  byte txData[8] = {0x10, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88};

  // CAN 메시지 전송
  byte sendStat = CAN.sendMsgBuf(0x123, 0, 8, txData);

  if (sendStat == CAN_OK) {
    Serial.println("Message Sent Successfully");
  } else {
    Serial.println("Error Sending Message");
  }

  delay(1000);
}
