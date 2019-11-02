import cv2
from random import randint


def func():

    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt2.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read() # intialize frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # necessary for detection
        print(gray)
        face = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in face:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            
            image_name = 'images/martin/my_image'+str(randint(0, 1000000))+'.png'
            cv2.imwrite(image_name, roi_color)

            color = (0, 255, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    func()