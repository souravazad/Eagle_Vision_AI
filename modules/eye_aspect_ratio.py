"""
============================================================
Eagle_Vision_AI v1.0
Module : Eye Aspect Ratio (EAR)
Author : Sourav Kumar Azad
============================================================
"""

import cv2
import mediapipe as mp
from math import hypot

from config import (
    CAMERA_INDEX,
    FRAME_WIDTH,
    FRAME_HEIGHT,
)

# --------------------------------------------------------
# Eye Landmark IDs
# --------------------------------------------------------

LEFT_EYE = [33, 160, 158, 133, 153, 144]

# P1 P2 P3 P4 P5 P6

# --------------------------------------------------------
# Distance Function
# --------------------------------------------------------

def euclidean_distance(p1, p2):
    return hypot(p2[0] - p1[0], p2[1] - p1[1])

# --------------------------------------------------------
# EAR Function
# --------------------------------------------------------

def calculate_ear(points):

    vertical1 = euclidean_distance(points[1], points[5])

    vertical2 = euclidean_distance(points[2], points[4])

    horizontal = euclidean_distance(points[0], points[3])

    ear = (vertical1 + vertical2) / (2.0 * horizontal)

    return ear

# --------------------------------------------------------
# MediaPipe
# --------------------------------------------------------

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

# --------------------------------------------------------
# Camera
# --------------------------------------------------------

cap = cv2.VideoCapture(CAMERA_INDEX)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

print("=" * 60)

print("Eye Aspect Ratio Module")

print("=" * 60)

# --------------------------------------------------------
# Main Loop
# --------------------------------------------------------

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        for face in results.multi_face_landmarks:

            h, w, _ = frame.shape

            eye_points = []

            for idx in LEFT_EYE:

                x = int(face.landmark[idx].x * w)

                y = int(face.landmark[idx].y * h)

                eye_points.append((x, y))

                cv2.circle(frame, (x, y), 3, (0,255,0), -1)

            ear = calculate_ear(eye_points)

            cv2.putText(
                frame,
                f"EAR : {ear:.3f}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

    cv2.imshow("Eye Aspect Ratio", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()

cv2.destroyAllWindows()