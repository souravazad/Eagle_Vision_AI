"""
=========================================================
Eagle Vision AI
Module : Face Database
Author : Sourav Kumar Azad
=========================================================
"""

import os
import sys
import pickle

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
# Database Folder
# =========================================================

EMBEDDING_DIR = os.path.join(
    BASE_DIR,
    "embeddings"
)

EMBEDDING_FILE = os.path.join(
    EMBEDDING_DIR,
    "students.pkl"
)

os.makedirs(
    EMBEDDING_DIR,
    exist_ok=True
)

# =========================================================
# Load Database
# =========================================================

def load_database():

    if not os.path.exists(EMBEDDING_FILE):
        return {}

    if os.path.getsize(EMBEDDING_FILE) == 0:
        return {}

    try:

        with open(
            EMBEDDING_FILE,
            "rb"
        ) as file:

            database = pickle.load(file)

        return database

    except Exception:

        return {}

# =========================================================
# Save Database
# =========================================================

def save_database(database):

    with open(
        EMBEDDING_FILE,
        "wb"
    ) as file:

        pickle.dump(
            database,
            file
        )

# =========================================================
# Add Student
# =========================================================

def add_student(
    student_name,
    embedding
):

    database = load_database()

    if student_name not in database:

        database[student_name] = []

    database[student_name].append(
        embedding
    )

    save_database(
        database
    )

    return len(
        database[student_name]
    )

# =========================================================
# Replace Face Embeddings
# =========================================================

def update_student(
    student_name,
    embeddings
):

    database = load_database()

    if student_name not in database:
        return False

    database[student_name] = embeddings

    save_database(
        database
    )

    return True

# =========================================================
# Rename Student
# =========================================================

def rename_student(
    old_name,
    new_name
):

    database = load_database()

    if old_name not in database:
        return False

    if new_name in database:
        return False

    database[new_name] = database.pop(
        old_name
    )

    save_database(
        database
    )

    return True

# =========================================================
# Delete Student
# =========================================================

def delete_student(
    student_name
):

    database = load_database()

    if student_name not in database:
        return False

    del database[student_name]

    save_database(
        database
    )

    return True

# =========================================================
# Get Student Embeddings
# =========================================================

def get_embedding(
    student_name
):

    database = load_database()

    return database.get(
        student_name,
        None
    )

# =========================================================
# Get All Students
# =========================================================

def get_all_students():

    return load_database()

# =========================================================
# Student Exists
# =========================================================

def student_exists(
    student_name
):

    database = load_database()

    return student_name in database

# =========================================================
# Total Students
# =========================================================

def total_students():

    database = load_database()

    return len(
        database
    )

# =========================================================
# Total Embeddings
# =========================================================

def total_embeddings():

    database = load_database()

    total = 0

    for embeddings in database.values():

        total += len(
            embeddings
        )

    return total

# =========================================================
# Clear Database
# =========================================================

def clear_database():

    save_database({})

# =========================================================
# Test Module
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("           Eagle Vision AI")
    print("            Face Database")
    print("=" * 60)

    database = load_database()

    print(
        f"Registered Students : {total_students()}"
    )

    print(
        f"Total Embeddings    : {total_embeddings()}"
    )

    print("-" * 60)

    if len(database) == 0:

        print("No students registered.")

    else:

        for student_name, embeddings in database.items():

            print(f"Student : {student_name}")

            print(
                f"Embeddings : {len(embeddings)}"
            )

            print("-" * 60)

    print("Database Loaded Successfully.")