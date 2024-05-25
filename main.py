import cv2 as cv
import sys

VIDEO_FPS = 25

# open the video
cap = cv.VideoCapture('poplar_videos/poplar_2.MOV')
if not cap.isOpened():
    print("Cannot open video file", file=sys.stderr)
    exit()

frame_count = 0
current_sec_avg = 0
previous_sec_avg = 0

count_1 = 0
count_0 = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # convert to grayscale
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # define region of interest
    #roi = frame[500:600, 750:850]
    roi = frame[500:520, 750:770]

    # draw rectangle
    #cv.rectangle(frame, (500, 750), (600, 850), (255, 0, 0), 2)

    # get average pixel value of ROI
    avg = cv.mean(roi)[0]
    if frame_count != 0 and frame_count % VIDEO_FPS == 0:
        current_sec_avg /= VIDEO_FPS
        if previous_sec_avg != 0:
            if current_sec_avg < previous_sec_avg:
                print(0)
                count_0 += 1
            else:
                print(1)
                count_1 += 1

        previous_sec_avg = current_sec_avg
        current_sec_avg = 0

    current_sec_avg += avg


    #cv.imshow('Frame', roi)
    #if cv.waitKey(40) & 0xFF == ord('q'):
    #    break
    #print(frame.shape)
    frame_count += 1

print("Count 0: ", count_0, " Count 1: ", count_1)