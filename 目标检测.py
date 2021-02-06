import cv2

cap = cv2.VideoCapture("video/test.mp4")
fps = int(cap.get(cv2.CAP_PROP_FPS))#读取视频FPS值
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('video/output1.mp4',-1, fps, size)

while True:
    success,video = cap.read()
    cv2.imshow("video",video)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
