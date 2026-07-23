"""
=========================================================
Eagle_Vision_AI
AI Classroom Monitoring System
Author : Sourav Kumar Azad
=========================================================
"""

import time
import cv2


# =========================================================
# Import Configuration
# =========================================================

from config import (
    CAMERA_INDEX,
    FRAME_WIDTH,
    FRAME_HEIGHT,
    WINDOW_NAME
)

# =========================================================
# Import Modules
# =========================================================

from modules.face_recognition_v2 import recognize_faces

from modules.eye_monitor import monitor_eye

from modules.drawing_utils import (
    draw_face,
    draw_eye_status,
    draw_dashboard,
    draw_fps,
    draw_datetime,
    draw_footer
)

from modules.face_database import total_students

from modules.attendance_manager import (
    total_attendance_today
)

# =========================================================
# Initialize Camera
# =========================================================

camera = cv2.VideoCapture(CAMERA_INDEX)

camera.set(
    cv2.CAP_PROP_FRAME_WIDTH,
    FRAME_WIDTH
)

camera.set(
    cv2.CAP_PROP_FRAME_HEIGHT,
    FRAME_HEIGHT
)

# =========================================================
# Camera Check
# =========================================================

if not camera.isOpened():

    print("=" * 60)
    print("Unable to Open Camera")
    print("=" * 60)

    exit()

# =========================================================
# FPS Variable
# =========================================================

previous_time = time.time()

# =========================================================
# Startup Banner
# =========================================================

print("=" * 60)
print("Eagle_Vision_AI")
print("AI Classroom Monitoring System")
print("=" * 60)
print(f"Registered Students : {total_students()}")
print(f"Today's Attendance  : {total_attendance_today()}")
print("Press ESC to Exit")
print("=" * 60)

# =========================================================
# Main Loop
# =========================================================

while True:

    success, frame = camera.read()

    if not success:
        break

    # =====================================================
    # Face Recognition
    # =====================================================

    persons = recognize_faces(frame)

    # =====================================================
    # Eye Monitoring
    # =====================================================

    eye_data = monitor_eye(frame)
    

    # =====================================================
    # Draw Face Boxes
    # =====================================================

    for person in persons:

        draw_face(
            frame,
            person
        )

    # =====================================================
    # Dashboard
    # =====================================================

    draw_dashboard(
        frame,
        len(persons)
    )

    # =====================================================
    # Eye Information
    # =====================================================

    draw_eye_status(
        frame,
        eye_data
    )

    # =====================================================
    # Registered Students
    # =====================================================

    cv2.putText(

        frame,

        f"Registered Students : {total_students()}",

        (20, 280),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.7,

        (0, 255, 255),

        2

    )

    # =====================================================
    # Attendance Today
    # =====================================================

    cv2.putText(

        frame,

        f"Today's Attendance : {total_attendance_today()}",

        (20, 315),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.7,

        (0, 255, 0),

        2

    )

    # =====================================================
    # FPS Calculation
    # =====================================================
    current_time = time.time()
    fps = 1.0 / max(current_time - previous_time, 0.0001)
    previous_time = current_time
    draw_fps(
    frame,
    fps
    )

    # =====================================================
    # Date & Time
    # =====================================================

    draw_datetime(
        frame
    )

    # =====================================================
    # Footer
    # =====================================================

    draw_footer(
        frame
    )

    # =====================================================
    # Display Window
    # =====================================================

    cv2.imshow(

        WINDOW_NAME,

        frame

    )

    # =====================================================
    # Exit Key
    # =====================================================

    key = cv2.waitKey(1) & 0xFF

    if key == 27:

        break

# =========================================================
# Cleanup
# =========================================================

camera.release()

cv2.destroyAllWindows()

print()
print("=" * 60)
print("Eagle_Vision_AI Closed Successfully")
print("=" * 60)