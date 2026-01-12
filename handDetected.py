import cv2
import numpy as np
import mediapipe as mp

webcam_image = np.ndarray
rgb_tuple = tuple[int, int, int]


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


    def find_hands(self, img: webcam_image, draw_hands: bool = True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks and draw_hands:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)
        return img


if __name__ == '__main__':
    Detec = Detector()

    capture = cv2.VideoCapture(0)
    while True:
        _, image = capture.read()

        image = Detec.find_hands(image)

        cv2.imshow('Camera', image)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
