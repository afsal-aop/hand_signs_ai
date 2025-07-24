import cv2
import numpy as np
import mediapipe as mp
from tensorflow import keras

model = keras.models.load_model('gesture_model.h5')
class_labels = ['Hii', 'peace', 'rock', 'well done']

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)

def predict_sign(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            xs = [lm.x for lm in handLms.landmark]
            ys = [lm.y for lm in handLms.landmark]
            combined = np.array(xs + ys).reshape(1, -1)
            prediction = model.predict(combined)
            index = np.argmax(prediction)
            label = class_labels[index]
            prob = round(prediction[0][index] * 100, 2)
            return f"{label} ({prob}%)"
    return "No hand"
