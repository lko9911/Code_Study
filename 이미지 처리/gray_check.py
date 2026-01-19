import cv2

# 이미지 경로
img_path = "image.png"   

# 이미지 읽기 (grayscale)
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    raise ValueError("이미지를 불러올 수 없습니다.")

# 마우스 클릭 이벤트 함수
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        gray_value = img[y, x]   # y 먼저, x 나중!
        print(f"Clicked at (x={x}, y={y}) → Grayscale value: {gray_value}")

        # 클릭 위치 시각화 (원 표시)
        img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.circle(img_color, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("image", img_color)

# 창 생성
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_callback)

# 이미지 표시
cv2.imshow("image", img)

print("이미지를 클릭하세요. 종료하려면 'q' 키")

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

h, w = img.shape
print(f"Image size → width: {w}, height: {h}")