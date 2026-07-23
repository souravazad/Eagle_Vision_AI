"""
=========================================================
Eagle_Vision_AI v2.1
Module : Attendance Manager
Author : Sourav Kumar Azad
=========================================================
"""

import os
import sys
import sqlite3
from datetime import datetime

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
# Import Configuration
# =========================================================

from config import DATABASE_PATH

# =========================================================
# Ensure Database Folder Exists
# =========================================================

os.makedirs(
    os.path.dirname(DATABASE_PATH),
    exist_ok=True
)

# =========================================================
# Create Attendance Table
# =========================================================

def create_attendance_table():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_name TEXT NOT NULL,

            date TEXT NOT NULL,

            time TEXT NOT NULL
        )
        """
    )

    connection.commit()

    connection.close()

# =========================================================
# Mark Attendance
# =========================================================

def mark_attendance(student_name):

    create_attendance_table()

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    current_time = datetime.now().strftime(
        "%H:%M:%S"
    )

    cursor.execute(
        """
        SELECT id
        FROM attendance
        WHERE student_name=?
        AND date=?
        """,
        (
            student_name,
            today
        )
    )

    record = cursor.fetchone()

    # ------------------------------------
    # Already Marked
    # ------------------------------------

    if record is not None:

        connection.close()

        return False

    # ------------------------------------
    # Insert Attendance
    # ------------------------------------

    cursor.execute(
        """
        INSERT INTO attendance
        (
            student_name,
            date,
            time
        )
        VALUES
        (
            ?,?,?
        )
        """,
        (
            student_name,
            today,
            current_time
        )
    )

    connection.commit()

    connection.close()

    print()

    print("=" * 60)
    print("Attendance Marked Successfully")
    print("=" * 60)
    print(f"Student : {student_name}")
    print(f"Date    : {today}")
    print(f"Time    : {current_time}")
    print("=" * 60)

    return True

# =========================================================
# Attendance Status
# =========================================================

def attendance_exists(student_name):

    create_attendance_table()

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    cursor.execute(
        """
        SELECT id
        FROM attendance
        WHERE student_name=?
        AND date=?
        """,
        (
            student_name,
            today
        )
    )

    record = cursor.fetchone()

    connection.close()

    return record is not None

# =========================================================
# Total Attendance Today
# =========================================================

def total_attendance_today():

    create_attendance_table()

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE date=?
        """,
        (
            today,
        )
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

# =========================================================
# Test Module
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Attendance Manager")
    print("=" * 60)

    status = mark_attendance(
        "Sourav azad"
    )

    print()

    if status:

        print("Attendance Status : MARKED")

    else:

        print("Attendance Status : ALREADY MARKED")

    print()

    print(
        f"Today's Attendance : {total_attendance_today()}"
    )

    print("=" * 60)