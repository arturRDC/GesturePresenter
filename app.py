import cv2
import mediapipe as mp


cap = cv2.VideoCapture(0)
drawing_utils = mp.solutions.drawing_utils
hand_detector = mp.solutions.hands.Hands()
while True:
  _, frame = cap.read()
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  detection = hand_detector.process(rgb_frame)
  hands = detection.multi_hand_landmarks
  
  print(hands)
  if hands:
    for hand in hands:
      drawing_utils.draw_landmarks(frame, hand)

  cv2.imshow('Gesture presenter', frame)
  key = cv2.waitKey(10)
  if key == 27:  # ESC
    break
