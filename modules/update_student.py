"""
=========================================================
Eagle Vision AI
Module : Update Student
Author : Sourav Kumar Azad
=========================================================
"""

import os
import sys
import cv2
import time

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

from modules.face_database import (
    get_all_students,
    student_exists,
    rename_student,
    replace_student_embeddings,
    delete_student
)

from modules.insightface_engine import face_app

# =========================================================
# Capture New Face Embeddings
# =========================================================

def capture_face_embeddings(student_name):

    print("\nOpening Camera...")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        print("\nUnable to access webcam.")
        return None

    MAX_EMBEDDINGS = 20
    CAPTURE_DELAY = 1

    embeddings = []

    last_capture = 0

    print("\nLook at the camera.")
    print("Move your head slowly.")
    print("Press ESC to cancel.\n")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        faces = face_app.get(frame)

        cv2.putText(
            frame,
            f"Student : {student_name}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Captured : {len(embeddings)}/{MAX_EMBEDDINGS}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2
        )

        if len(faces) > 0:

            face = faces[0]

            x1, y1, x2, y2 = face.bbox.astype(int)

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            current_time = time.time()

            if (
                current_time - last_capture >= CAPTURE_DELAY
                and len(embeddings) < MAX_EMBEDDINGS
            ):

                embeddings.append(
                    face.embedding
                )

                print(
                    f"Captured {len(embeddings)}/{MAX_EMBEDDINGS}"
                )

                last_capture = current_time

        else:

            cv2.putText(
                frame,
                "No Face Detected",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        cv2.imshow(
            "Update Face Data",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == 27:

            embeddings = None
            break

        if len(embeddings) >= MAX_EMBEDDINGS:

            break

    cap.release()

    cv2.destroyAllWindows()

    return embeddings

# =========================================================
# Update Student
# =========================================================

def update_student():

    print("\n" + "=" * 55)
    print("        Eagle Vision AI")
    print("        Update Student")
    print("=" * 55)

    database = get_all_students()

    if len(database) == 0:

        print("\nNo students registered.")
        input("\nPress Enter to continue...")
        return

    student_list = list(database.keys())

    print("\nRegistered Students")
    print("-" * 55)

    for index, student in enumerate(
        student_list,
        start=1
    ):

        total_embeddings = len(
            database[student]
        )

        print(
            f"{index}. {student}"
        )

        print(
            f"   Total Embeddings : {total_embeddings}"
        )

        print("-" * 55)

    try:

        choice = int(
            input(
                "\nSelect Student Number : "
            )
        )

    except ValueError:

        print("\nInvalid input.")
        input("\nPress Enter to continue...")
        return

    if (
        choice < 1
        or
        choice > len(student_list)
    ):

        print("\nInvalid student.")
        input("\nPress Enter to continue...")
        return

    selected_student = student_list[
        choice - 1
    ]

    print()
    print(f"Selected Student : {selected_student}")

    print("\nUpdate Options")
    print("-" * 40)

    print("1. Update Student Name")
    print("2. Update Face Data")
    print("3. Update Name + Face Data")
    print("4. Delete Student")
    print("5. Cancel")

    try:

        option = int(
            input(
                "\nEnter Choice : "
            )
        )

    except ValueError:

        print("\nInvalid choice.")
        input("\nPress Enter to continue...")
        return
    
        # =====================================================
    # OPTION 1
    # Update Student Name
    # =====================================================

    if option == 1:

        print(f"\nCurrent Name : {selected_student}")

        new_name = input(
            "Enter New Name : "
        ).strip()

        if new_name == "":

            print("\nStudent name cannot be empty.")

        elif new_name == selected_student:

            print("\nNew name is the same as current name.")

        elif student_exists(new_name):

            print("\nStudent already exists.")

        else:

            success = rename_student(
                selected_student,
                new_name
            )

            if success:

                print("\n" + "=" * 55)
                print("Student Renamed Successfully")
                print("=" * 55)
                print(f"Old Name : {selected_student}")
                print(f"New Name : {new_name}")
                print("=" * 55)

            else:

                print("\nUnable to rename student.")

        input("\nPress Enter to continue...")

    # =====================================================
    # OPTION 2
    # Update Face Data
    # =====================================================

    elif option == 2:

        embeddings = capture_face_embeddings(
            selected_student
        )

        if embeddings is None:

            print("\nOperation cancelled.")

        elif len(embeddings) == 0:

            print("\nNo face captured.")

        else:

            success = replace_student_embeddings(
                selected_student,
                embeddings
            )

            if success:

                print("\n" + "=" * 55)
                print("Face Data Updated Successfully")
                print("=" * 55)
                print(f"Student : {selected_student}")
                print(f"Embeddings : {len(embeddings)}")
                print("=" * 55)

            else:

                print("\nUnable to update face data.")

        input("\nPress Enter to continue...")

    # =====================================================
    # OPTION 3
    # Update Name + Face Data
    # =====================================================

    elif option == 3:

        print(f"\nCurrent Name : {selected_student}")

        new_name = input(
            "Enter New Name : "
        ).strip()

        if new_name == "":

            print("\nStudent name cannot be empty.")
            input("\nPress Enter to continue...")
            return

        if (
            new_name != selected_student
            and
            student_exists(new_name)
        ):

            print("\nStudent already exists.")
            input("\nPress Enter to continue...")
            return

        embeddings = capture_face_embeddings(
            selected_student
        )

        if embeddings is None:

            print("\nOperation cancelled.")
            input("\nPress Enter to continue...")
            return

        if len(embeddings) == 0:

            print("\nNo face captured.")
            input("\nPress Enter to continue...")
            return

        rename_ok = True

        if new_name != selected_student:

            rename_ok = rename_student(
                selected_student,
                new_name
            )

        if rename_ok:

            success = replace_student_embeddings(
                new_name,
                embeddings
            )

            if success:

                print("\n" + "=" * 55)
                print("Student Updated Successfully")
                print("=" * 55)
                print(f"Student Name : {new_name}")
                print(f"Embeddings   : {len(embeddings)}")
                print("=" * 55)

            else:

                print("\nUnable to update embeddings.")

        else:

            print("\nUnable to rename student.")

        input("\nPress Enter to continue...")
        
        # =====================================================
    # OPTION 4
    # Delete Student
    # =====================================================

    elif option == 4:

        print("\n" + "=" * 55)
        print("WARNING")
        print("=" * 55)
        print(f"You are about to delete : {selected_student}")
        print("This action cannot be undone.")
        print("=" * 55)

        confirm = input(
            "\nType YES to confirm : "
        ).strip()

        if confirm.upper() != "YES":

            print("\nDeletion cancelled.")
            input("\nPress Enter to continue...")
            return

        success = delete_student(
            selected_student
        )

        if success:

            print("\n" + "=" * 55)
            print("Student Deleted Successfully")
            print("=" * 55)
            print(f"Deleted Student : {selected_student}")
            print("=" * 55)

        else:

            print("\nUnable to delete student.")

        input("\nPress Enter to continue...")

    # =====================================================
    # OPTION 5
    # Cancel
    # =====================================================

    elif option == 5:

        print("\nOperation Cancelled.")

        input("\nPress Enter to continue...")

    # =====================================================
    # Invalid Option
    # =====================================================

    else:

        print("\nInvalid Choice.")

        input("\nPress Enter to continue()...")


# =========================================================
# Run
# =========================================================

if __name__ == "__main__":

    update_student()