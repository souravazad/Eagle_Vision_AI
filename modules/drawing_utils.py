"""
=========================================================
Eagle_Vision_AI
Module : Drawing Utilities
Author : Sourav Kumar Azad
=========================================================
"""

import cv2
from datetime import datetime


# =========================================================
# Draw Face
# =========================================================

def draw_face(frame, person):

    x1, y1, x2, y2 = person["bbox"]

    name = person["name"]

    similarity = person["similarity"]

    matched = person["matched"]

    confidence = int(similarity * 100)

    if matched:

        color = (0, 255, 0)

        status = "Recognized"

    else:

        color = (0, 0, 255)

        status = "Unknown"

    # Face Box
    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        2
    )

    # Student Name
    cv2.putText(
        frame,
        name,
        (x1, y1 - 45),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        color,
        2
    )

    # Confidence
    cv2.putText(
        frame,
        f"Confidence : {confidence}%",
        (x1, y1 - 22),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        color,
        2
    )

    # Status
    cv2.putText(
        frame,
        status,
        (x1, y2 + 22),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        color,
        2
    )


# =========================================================
# Draw Eye Status
# =========================================================

def draw_eye_status(frame, eye_data):

    ear = eye_data["EAR"]

    blink = eye_data["blink_count"]

    drowsy = eye_data["drowsy"]

    cv2.putText(
        frame,
        f"EAR : {ear:.2f}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Blinks : {blink}",
        (20, 165),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    if drowsy:

        text = "DROWSY"

        color = (0, 0, 255)

    else:

        text = "ALERT"

        color = (0, 255, 0)

    cv2.putText(
        frame,
        f"Status : {text}",
        (20, 200),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        color,
        2
    )


# =========================================================
# Draw Dashboard
# =========================================================

def draw_dashboard(frame, total_faces):

    cv2.putText(
        frame,
        "Eagle_Vision_AI",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "AI Classroom Monitoring System",
        (20, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Faces Detected : {total_faces}",
        (20, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 0),
        2
    )


# =========================================================
# Draw FPS
# =========================================================

def draw_fps(frame, fps):

    cv2.putText(
        frame,
        f"FPS : {fps:.1f}",
        (20, 245),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )


# =========================================================
# Draw Date & Time
# =========================================================

def draw_datetime(frame):

    now = datetime.now()

    date = now.strftime("%d-%b-%Y")

    current_time = now.strftime("%H:%M:%S")

    cv2.putText(
        frame,
        date,
        (930, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        current_time,
        (930, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )


# =========================================================
# Draw Footer
# =========================================================

def draw_footer(frame):

    height = frame.shape[0]

    cv2.rectangle(
        frame,
        (0, height - 35),
        (frame.shape[1], height),
        (40, 40, 40),
        -1
    )

    cv2.putText(
        frame,
        "InsightFace  |  Attendance  |  Eye Monitor  |  AI Classroom Monitoring",
        (20, height - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 255, 255),
        2
    )