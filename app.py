import cv2
import mediapipe as mp
import pyautogui
import time
import argparse

def calculate_distance(p1, p2):
  return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

def main(show_output, invert_controls):
  cap = cv2.VideoCapture(0)
  drawing_utils = mp.solutions.drawing_utils
  hand_detector = mp.solutions.hands.Hands()

  last_click_time = 0
  click_cooldown = 0.4  # Cooldown time in seconds

  while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    f_height, f_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detection = hand_detector.process(rgb_frame)
    hands = detection.multi_hand_landmarks
    
    if hands:
      for hand in hands:
        if show_output:
          drawing_utils.draw_landmarks(frame, hand)
        landmarks = hand.landmark
        
        wrist = landmarks[0]
        middle_finger_knucle = landmarks[12]
        reference_distance = calculate_distance(wrist, middle_finger_knucle)
        
        index_finger_tip = landmarks[8]
        middle_finger_tip = landmarks[12]
        thumb_tip = landmarks[4]
        
        index_thumb_distance = calculate_distance(index_finger_tip, thumb_tip)
        middle_thumb_distance = calculate_distance(middle_finger_tip, thumb_tip)
        
        index_relative_distance = index_thumb_distance / reference_distance
        middle_relative_distance = middle_thumb_distance / reference_distance
        
        current_time = time.time()
        if (current_time - last_click_time) > click_cooldown:
          if index_relative_distance < 0.12:
            key = 'right' if invert_controls else 'left'
            pyautogui.press(key)
            last_click_time = current_time
          elif middle_relative_distance < 0.2:
            key = 'left' if invert_controls else 'right'
            pyautogui.press(key)
            last_click_time = current_time
        
        if show_output:
          for point in [index_finger_tip, middle_finger_tip, thumb_tip]:
            x = int(point.x * f_width)
            y = int(point.y * f_height)
            cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))

    if show_output:
      cv2.imshow('Gesture presenter', frame)
      key = cv2.waitKey(10)
      if key == 27:  # ESC
        break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Gesture-based presenter control")
  parser.add_argument("--show-output", action="store_true", help="Show camera output")
  parser.add_argument("--invert-controls", action="store_true", help="Invert finger controls")
  args = parser.parse_args()

  main(args.show_output, args.invert_controls)