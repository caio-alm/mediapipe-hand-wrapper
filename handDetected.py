import cv2
import numpy as np
import mediapipe as mp

webcam_image = np.ndarray
rgb_tuple = tuple[int, int, int]
signals = {
    "Peace": [False, True, True, False, False],
    "Hang Loose": [True, False, False, False, True],
    "Rock": [False, True, False, False, True]
}


class Detector:
    def __init__(self,
                 mode: bool = False,
                 num_hands: int = 2,
                 model_complexity: int = 1,
                 min_detection_confidence: float = 0.5,
                 min_tracking_confidence: float = 0.5):

        self.mode = mode
        self.max_num_hands = num_hands
        self.complexity = model_complexity
        self.detection_confidence = min_detection_confidence
        self.tracking_confidence = min_tracking_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode,
                                         self.max_num_hands,
                                         self.complexity,
                                         self.detection_confidence,
                                         self.tracking_confidence)

        self.mp_draw = mp.solutions.drawing_utils


    def findHands(self, img: webcam_image, draw_hands: bool = True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks and draw_hands:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)
        return img


    def raisedFingers(self, hand):
        fingers = []
        fingersHand = [4, 8, 12, 16, 20]

        if hand.landmark[fingersHand[0]].x > hand.landmark[fingersHand[0]-2].x:
            fingers.append(True)

        else:
            fingers.append(False)

        for f in range(1, 5):
            if hand.landmark[fingersHand[f]].y < hand.landmark[fingersHand[f] - 2].y:
                fingers.append(True)

            else:
                fingers.append(False)

        return fingers


if __name__ == '__main__':
    Detec = Detector()

    capture = cv2.VideoCapture(0)
    while True:
        _, image = capture.read()

        image = Detec.findHands(image)

        if Detec.results and Detec.results.multi_hand_landmarks:
            hand_rigth_obj = Detec.results.multi_hand_landmarks[0]

            raisedFingers = Detec.raisedFingers(hand_rigth_obj)

            print(raisedFingers)

            total = raisedFingers.count(1)
            cv2.putText(image, f'Rigth Fingers: {total}', (30, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 1)

            for s, v in signals.items():
                if raisedFingers == v:
                    cv2.putText(image, f'Signal: {s}', (30, 60), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 1)

        cv2.imshow('Camera', image)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
