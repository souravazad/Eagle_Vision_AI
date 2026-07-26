"""
=========================================================
Eagle Vision AI
Module : Register Student
Author : Sourav Kumar Azad
=========================================================
"""

import os
import sys
import cv2
import time


# ==========================================================
# Add Project Root
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)

# ==========================================================
# Import Project Modules
# ==========================================================

from modules.insightface_engine import face_app

from modules.face_database import (
    add_student,
    student_exists,
    total_students
)

# ==========================================================
# Register Student
# ==========================================================

def register_student():

    print("\n" + "=" * 60)
    print("        Eagle Vision AI")
    print("      Student Registration")
    print("=" * 60)

    # ------------------------------------------------------
    # Student Name
    # ------------------------------------------------------

    student_name = input(
        "\nEnter Student Name : "
    ).strip()

    if student_name == "":

        print("\nStudent name cannot be empty.")
        return

    # ------------------------------------------------------
    # Duplicate Check
    # ------------------------------------------------------

    if student_exists(student_name):

        print("\nStudent already exists.")
        return

    # ------------------------------------------------------
    # Camera
    # ------------------------------------------------------

    print("\nOpening Camera...")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


    if not cap.isOpened():

        print("\nUnable to access webcam.")
        return

    # ------------------------------------------------------
    # Variables
    # ------------------------------------------------------

    embeddings = []

    MAX_EMBEDDINGS = 20

    capture_delay = 1

    last_capture_time = 0

    print("\nLook at the camera.")

    print("Move your head slowly.")

    print("Press ESC anytime to cancel.\n")

    while True:

        ret, frame = cap.read()

        if not ret:
            print("\nUnable to read camera frame.")
            break

        frame = cv2.flip(
            frame,
            1
        )

        faces = face_app.get(frame)

        # --------------------------------------------------
        # Display Instructions
        # --------------------------------------------------

        cv2.putText(

            frame,

            f"Student : {student_name}",

            (20,40),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0,255,0),

            2

        )

        cv2.putText(

            frame,

            f"Captured : {len(embeddings)}/{MAX_EMBEDDINGS}",

            (20,80),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (255,255,0),

            2

        )

        cv2.putText(

    frame,

    "Look Straight | Slowly Move Your Head",

    (20,120),

    cv2.FONT_HERSHEY_SIMPLEX,

    0.6,

    (255,255,255),

    2

        )

        cv2.putText(

            frame,

            "ESC = Cancel",

            (20,160),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            (0,0,255),

            2

        )

        # --------------------------------------------------
        # Face Found
        # --------------------------------------------------

        if len(faces) > 0:

            face = faces[0]

            bbox = face.bbox.astype(int)

            x1, y1, x2, y2 = bbox

            cv2.rectangle(

                frame,

                (x1, y1),

                (x2, y2),

                (0, 255, 0),

                2

            )

            current_time = time.time()

            if (

                current_time - last_capture_time >= capture_delay

                and len(embeddings) < MAX_EMBEDDINGS

            ):

                embedding = face.embedding

                embeddings.append(

                    embedding

                )

                print(

                    f"Captured {len(embeddings)}/{MAX_EMBEDDINGS}"

                )

                last_capture_time = current_time

        else:

            cv2.putText(

                frame,

                "No Face Detected",

                (20, 200),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.8,

                (0, 0, 255),

                2

            )
        # --------------------------------------------------
        # Show Window
        # --------------------------------------------------

        cv2.imshow(

            "Register Student",

            frame

        )

        # --------------------------------------------------
        # ESC Key
        # --------------------------------------------------

        key = cv2.waitKey(1) & 0xFF

        if key == 27:

            print("\nRegistration Cancelled.")

            break

        # --------------------------------------------------
        # Registration Completed
        # --------------------------------------------------

        if len(embeddings) >= MAX_EMBEDDINGS:

            break
    # ======================================================
    # Close Camera
    # ======================================================

    cap.release()

    cv2.destroyAllWindows()

    # ======================================================
    # No Face Captured
    # ======================================================

    if len(embeddings) == 0:

        print("\nNo face captured.")

        return

    # ======================================================
    # Save Embeddings
    # ======================================================

    print("\nSaving Student...")

    for embedding in embeddings:

        add_student(

            student_name,

            embedding

        )

    # ======================================================
    # Registration Complete
    # ======================================================

    print()

    print("=" * 60)
    print("Student Registered Successfully")
    print("=" * 60)

    print(f"Student Name        : {student_name}")
    print(f"Embeddings Saved    : {len(embeddings)}")
    print(f"Total Students      : {total_students()}")

    print("=" * 60)

    input("\nPress Enter to continue...")