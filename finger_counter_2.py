import cv2
import mediapipe as mp
import pyautogui  
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Initially set finger count to 0 for each cap
    fingerCount = 0

    if results.multi_hand_landmarks:

      for hand_landmarks in results.multi_hand_landmarks:
        # Get hand index to check label (left or right)
        handIndex = results.multi_hand_landmarks.index(hand_landmarks)
        handLabel = results.multi_handedness[handIndex].classification[0].label

        # Set variable to keep landmarks positions (x and y)
        handLandmarks = []

        # Fill list with x and y positions of each landmark
        for landmarks in hand_landmarks.landmark:
          handLandmarks.append([landmarks.x, landmarks.y])

        # Test conditions for each finger: Count is increased if finger is 
        #   considered raised.
        # Thumb: TIP x position must be greater or lower than IP x position, 
        #   deppeding on hand label.
        if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
          fingerCount = fingerCount+1
        elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
          fingerCount = fingerCount+1

        # Other fingers: TIP y position must be lower than PIP y position, 
        #   as image origin is in the upper left corner.
        if handLandmarks[8][1] < handLandmarks[6][1]:       #Index finger
          fingerCount = fingerCount+1
        if handLandmarks[12][1] < handLandmarks[10][1]:     #Middle finger
          fingerCount = fingerCount+1
        if handLandmarks[16][1] < handLandmarks[14][1]:     #Ring finger
          fingerCount = fingerCount+1
        if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
          fingerCount = fingerCount+1

        # Draw hand landmarks 
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        #make finger counters
        if fingerCount == 10:
            count10 = count10+1
            print("10 count" + str(count10))
        if fingerCount == 9:
              count9 = count9+1
              print("9 count" + str(count9))
        if fingerCount == 8:
              count8 = count8+1
              print("8 count" + str(count8))
        if fingerCount == 7:
              count7 = count7+1
              print("7 count" + str(count7))
        if fingerCount == 6:
              count6 = count6+1
              print("6 count" + str(count6))
        if fingerCount == 5:
              count5 = count5+1
              print("5 count" + str(count5))
        if fingerCount == 4:
              count4 = count4+1
              print("4 count" + str(count4))
        if fingerCount == 3:
              count3 = count3+1
              print("3 count" + str(count3))
        if fingerCount == 2:
              count2 = count2+1
              print("2 count" + str(count2))
        if fingerCount == 1:
              count1 = count1+1
              print("1 count" + str(count1))
        if count6==15:
              pyautogui.hotkey('command','r')
        if count5==15:
              print("We are doing action related to finger 5")
              pyautogui.hotkey('fn','f')
        if count4==15:
              pyautogui.hotkey('command','m')
        if count3 >= 10:
              pyautogui.scroll(10) 
        if count2 >= 10:
              pyautogui.scroll(-10)
        if fingerCount ==0: 
          count1 = 0
          count2 = 0
          count3 = 0
          count4 = 0
          count5 = 0
          count6 = 0
          count7 = 0
          count8 = 0
          count9 = 0
          count10 = 0
    # Display finger count
    cv2.putText(image, str(fingerCount), (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)
    # Display image
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
