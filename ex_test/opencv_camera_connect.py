#   카메라 연결 코드
import cv2

# opencv python 코딩 기본 틀
capture = cv2.VideoCapture(0) #캠으로 부터 가져오겠다 2개 사용시 0 , 1설정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 무한루프
while True:
    ret, frame = capture.read()     
    cv2.imshow("original", frame)   
    if cv2.waitKey(1) == ord('q'): 
            break

capture.release()                   # 캡처 객체를 없애줌
cv2.destroyAllWindows()             # 모든 영상 창을 닫아줌