import cv2, time

video = cv2.VideoCapture(0)
cnt = 0

while True:
    cnt= cnt+1
    check,frame= video.read()
    print(check)
    print(frame)

    cv2.imshow("Video",frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows
