import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(0)
drawing_utils = mp.solutions.drawing_utils
hand_detector = mp.solutions.hands.Hands()

last_click_time = 0
click_cooldown = 0.4  # Cooldown time in seconds

def calculate_distance(p1, p2):
  return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

while True:
  _, frame = cap.read()
  frame = cv2.flip(frame, 1)
  f_height, f_width, _ = frame.shape
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  detection = hand_detector.process(rgb_frame)
  hands = detection.multi_hand_landmarks
  screen_width, screen_height = pyautogui.size()
  
  if hands:
    for hand in hands:
      drawing_utils.draw_landmarks(frame, hand)
      landmarks = hand.landmark
      
      # Get reference distance (distance between wrist and middle finger tip)
      wrist = landmarks[0]
      middle_finger_knucle = landmarks[12]
      reference_distance = calculate_distance(wrist, middle_finger_knucle)
      
      # Get index finger tip, middle finger tip, and thumb tip
      index_finger_tip = landmarks[8]
      middle_finger_tip = landmarks[12]
      thumb_tip = landmarks[4]
      
      # Calculate distances
      index_thumb_distance = calculate_distance(index_finger_tip, thumb_tip)
      middle_thumb_distance = calculate_distance(middle_finger_tip, thumb_tip)
      
      # Calculate relative distances
      index_relative_distance = index_thumb_distance / reference_distance
      middle_relative_distance = middle_thumb_distance / reference_distance
      
      current_time = time.time()
      if (current_time - last_click_time) > click_cooldown:
        if index_relative_distance < 0.12:
          pyautogui.press('left')
          last_click_time = current_time
        elif middle_relative_distance < 0.2:
          pyautogui.press('right')
          last_click_time = current_time
      
      # Draw circles on finger tips and thumb tip
      for point in [index_finger_tip, middle_finger_tip, thumb_tip]:
        x = int(point.x * f_width)
        y = int(point.y * f_height)
        cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))

  cv2.imshow('Gesture presenter', frame)
  key = cv2.waitKey(10)
  if key == 27:  # ESC
    break

cap.release()
cv2.destroyAllWindows()