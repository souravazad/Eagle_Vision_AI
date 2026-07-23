"""
=========================================================
Eagle_Vision_AI v2.1
Module : Professional Face Matcher
Author : Sourav Kumar Azad
=========================================================
"""

import os
import sys
import numpy as np

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

from modules.face_database import get_all_students

# =========================================================
# Configuration
# =========================================================

MATCH_THRESHOLD = 0.65

# =========================================================
# Cosine Similarity
# =========================================================

def cosine_similarity(embedding1, embedding2):
    """
    Returns cosine similarity between two embeddings.
    """

    embedding1 = np.array(embedding1)
    embedding2 = np.array(embedding2)

    dot_product = np.dot(
        embedding1,
        embedding2
    )

    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)

    similarity = dot_product / (norm1 * norm2)

    return float(similarity)

# =========================================================
# Find Best Match
# =========================================================

def find_best_match(live_embedding):

    database = get_all_students()

    best_name = "Unknown"

    best_similarity = -1.0

    for student_name, embeddings in database.items():

        for stored_embedding in embeddings:

            similarity = cosine_similarity(
                live_embedding,
                stored_embedding
            )

            if similarity > best_similarity:

                best_similarity = similarity

                best_name = student_name

    return best_name, best_similarity

# =========================================================
# Recognition Function
# =========================================================

def recognize_embedding(live_embedding):

    name, similarity = find_best_match(
        live_embedding
    )

    if similarity >= MATCH_THRESHOLD:

        return {

            "matched": True,
            "name": name,
            "similarity": round(similarity, 3)

        }

    return {

        "matched": False,
        "name": "Unknown",
        "similarity": round(similarity, 3)

    }

# =========================================================
# Test
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Professional Face Matcher")
    print("=" * 60)

    database = get_all_students()

    if len(database) == 0:

        print("No students registered.")

        sys.exit()

    print()

    print("Registered Students")

    print()

    for student, embeddings in database.items():

        print(student)

        print(f"Embeddings : {len(embeddings)}")

        print()

    print("=" * 60)

    print("Module Ready Successfully.")