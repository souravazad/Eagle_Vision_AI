"""
====================================================
 Eagle Vision AI
 Student Management System
====================================================
Author  : Sourav Kumar Azad
Version : 1.0
====================================================
"""


import os
from modules.register_student import register_student
from modules.update_student import update_student

from modules.face_database import (
    get_all_students,
    delete_student
)


# ==========================================================
# Clear Screen
# ==========================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ==========================================================
# Banner
# ==========================================================

def banner():

    clear_screen()

    print("=" * 55)
    print("        Eagle Vision AI")
    print("    Student Management System")
    print("=" * 55)


# ==========================================================
# View Students (READ)
# ==========================================================

def view_students():

    banner()

    print("\nRegistered Students\n")

    database = get_all_students()

    if len(database) == 0:

        print("No students found.")

    else:

        print(f"Total Students : {len(database)}\n")

        print("-" * 55)

        for index, (student_name, embeddings) in enumerate(
            database.items(),
            start=1
        ):

            print(f"{index}. {student_name}")
            print(f"   Total Embeddings : {len(embeddings)}")
            print("-" * 55)

    input("\nPress Enter to continue...")


# ==========================================================
# ==========================================================
# Delete Student (DELETE)
# ==========================================================

def delete_existing_student():

    banner()

    database = get_all_students()

    if len(database) == 0:

        print("\nNo students found.")
        input("\nPress Enter to continue...")
        return

    print("\nRegistered Students\n")

    student_list = list(database.items())

    print("-" * 55)
    print("{:<5} {:<20} {:<15}".format(
        "No.",
        "Student Name",
        "Embeddings"
    ))
    print("-" * 55)

    for index, (student_name, embeddings) in enumerate(
        student_list,
        start=1
    ):

        print("{:<5} {:<20} {:<15}".format(
            index,
            student_name,
            len(embeddings)
        ))

    print("-" * 55)

    try:

        choice = int(
            input("\nSelect Student Number : ")
        )

    except ValueError:

        print("\nPlease enter a valid number.")
        input("\nPress Enter to continue...")
        return

    if choice < 1 or choice > len(student_list):

        print("\nInvalid Student Number.")
        input("\nPress Enter to continue...")
        return

    student_name = student_list[choice - 1][0]

    confirm = input(
        f"\nDelete '{student_name}' ? (Y/N): "
    ).strip().upper()

    if confirm != "Y":

        print("\nDeletion Cancelled.")
        input("\nPress Enter to continue...")
        return

    if delete_student(student_name):

        print(f"\n'{student_name}' deleted successfully.")

    else:

        print("\nUnable to delete student.")

    input("\nPress Enter to continue...")



# ==========================================================
# Main Menu
# ==========================================================

def main():

    while True:

        banner()

        print("1. Register Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        print("=" * 55)

        choice = input("Enter your choice : ").strip()

        if choice == "1":
            register_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            update_student()

        elif choice == "4":

            delete_existing_student()

        elif choice == "5":

            print("\nThank you for using Eagle Vision AI.")
            break

        else:

            print("\nInvalid Choice.")
            input("\nPress Enter to continue...")


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    main()