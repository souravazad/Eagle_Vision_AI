"""
=========================================================
Eagle Vision AI
Module : Update Student
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
# Import Face Database
# =========================================================

from modules.face_database import (
    get_all_students,
    student_exists,
    rename_student
)

# =========================================================
# Update Student
# =========================================================

def update_student():

    print("\n" + "=" * 55)
    print("        Eagle Vision AI")
    print("        Update Student")
    print("=" * 55)

    # =====================================================
    # Load Students
    # =====================================================

    database = get_all_students()

    if len(database) == 0:

        print("\nNo students registered.")
        input("\nPress Enter to continue...")
        return

    # =====================================================
    # Student List
    # =====================================================

    student_list = list(database.keys())

    print("\nRegistered Students")
    print("-" * 55)

    for index, student_name in enumerate(
        student_list,
        start=1
    ):

        print(f"{index}. {student_name}")

    print("-" * 55)

    # =====================================================
    # Select Student
    # =====================================================

    try:

        choice = int(
            input("\nSelect Student Number : ")
        )

    except ValueError:

        print("\nInvalid Input.")
        input("\nPress Enter to continue...")
        return

    if choice < 1 or choice > len(student_list):

        print("\nInvalid Student Number.")
        input("\nPress Enter to continue...")
        return

    selected_student = student_list[
        choice - 1
    ]

    # =====================================================
    # Update Menu
    # =====================================================

    print("\nSelected Student :", selected_student)

    print("\nWhat do you want to update?")
    print("-" * 40)
    print("1. Student Name")
    print("2. Face Data (Coming Soon)")
    print("3. Name + Face Data (Coming Soon)")
    print("4. Cancel")

    try:

        update_choice = int(
            input("\nEnter Choice : ")
        )

    except ValueError:

        print("\nInvalid Choice.")
        input("\nPress Enter to continue...")
        return

    # =====================================================
    # Rename Student
    # =====================================================

    if update_choice == 1:

        new_name = input(
            "\nEnter New Student Name : "
        ).strip()

        if new_name == "":

            print("\nStudent name cannot be empty.")
            input("\nPress Enter to continue...")
            return

        if new_name == selected_student:

            print("\nNew name is same as old name.")
            input("\nPress Enter to continue...")
            return

        if student_exists(new_name):

            print("\nStudent already exists.")
            input("\nPress Enter to continue...")
            return

        success = rename_student(
            selected_student,
            new_name
        )

        if success:

            print("\nStudent Updated Successfully.")
            print(f"Old Name : {selected_student}")
            print(f"New Name : {new_name}")

        else:

            print("\nUnable to update student.")

    # =====================================================
    # Face Update
    # =====================================================

    elif update_choice == 2:

        print("\nFace Data Update")
        print("Coming Soon...")

    # =====================================================
    # Name + Face Update
    # =====================================================

    elif update_choice == 3:

        print("\nName + Face Data Update")
        print("Coming Soon...")

    # =====================================================
    # Cancel
    # =====================================================

    elif update_choice == 4:

        print("\nUpdate Cancelled.")

    else:

        print("\nInvalid Choice.")

    input("\nPress Enter to continue...")

# =========================================================
# Test Module
# =========================================================

if __name__ == "__main__":

    update_student()