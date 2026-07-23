"""
=========================================================
Eagle_Vision_AI
Module : Professional Live Face Recognition
Author : Sourav Kumar Azad
=========================================================
"""

import os
import sys

# =========================================================
# Add Project Root
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)

# =========================================================
# Import Modules
# =========================================================

from modules.insightface_engine import face_app
from modules.face_matcher import recognize_embedding
from modules.attendance_manager import mark_attendance

# =========================================================
# Live Recognition
# =========================================================

def recognize_faces(frame):

    people = []

    faces = face_app.get(frame)

    for face in faces:

        embedding = face.embedding

        recognition = recognize_embedding(
            embedding
        )

        matched = recognition["matched"]

        name = recognition["name"]

        similarity = recognition["similarity"]

        confidence = int(
            similarity * 100
        )

        attendance_status = ""

        if matched:

            marked = mark_attendance(
                name
            )

            if marked:

                attendance_status = "MARKED"

            else:

                attendance_status = "ALREADY MARKED"

        else:

            attendance_status = "UNKNOWN"

        x1, y1, x2, y2 = face.bbox.astype(int)

        person = {

            "name": name,

            "matched": matched,

            "similarity": similarity,

            "confidence": confidence,

            "attendance": attendance_status,

            "bbox": (

                x1,
                y1,
                x2,
                y2

            )

        }

        people.append(
            person
        )

    return people


# =========================================================
# Module Test
# =========================================================

if __name__ == "__main__":

    import cv2

    camera = cv2.VideoCapture(0)

    print("=" * 60)
    print("Eagle_Vision_AI Professional Recognition")
    print("=" * 60)

    while True:

        success, frame = camera.read()

        if not success:
            break

        people = recognize_faces(frame)

        for person in people:

            x1, y1, x2, y2 = person["bbox"]

            if person["matched"]:

                color = (0,255,0)

            else:

                color = (0,0,255)

            cv2.rectangle(

                frame,

                (x1,y1),

                (x2,y2),

                color,

                2

            )

            cv2.putText(

                frame,

                person["name"],

                (x1,y1-45),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.70,

                color,

                2

            )

            cv2.putText(

                frame,

                f'Confidence : {person["confidence"]}%',

                (x1,y1-20),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.60,

                color,

                2

            )

            cv2.putText(

                frame,

                person["attendance"],

                (x1,y2+25),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.60,

                color,

                2

            )

        cv2.imshow(

            "Eagle_Vision_AI Professional Recognition",

            frame

        )

        key = cv2.waitKey(1)

        if key == 27:

            break

    camera.release()

    cv2.destroyAllWindows()

    print()

    print("=" * 60)
    print("Recognition Module Closed")
    print("=" * 60)