import os

# ==========================================
# Project Root Directory
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# ==========================================
# Database Configuration
# ==========================================

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "database",
    "attendance.db"
)

# ==========================================
# Model Configuration
# ==========================================

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

FACE_RECOGNIZER_MODEL = os.path.join(
    MODEL_DIR,
    "trainer.yml"
)

FACE_CASCADE_PATH = os.path.join(
    MODEL_DIR,
    "haarcascade_frontalface_default.xml"
)

# ==========================================
# Dataset Configuration
# ==========================================

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset"
)

# ==========================================
# Logs Configuration
# ==========================================

LOG_DIR = os.path.join(
    BASE_DIR,
    "logs"
)

# ==========================================
# Reports Configuration
# ==========================================

REPORT_DIR = os.path.join(
    BASE_DIR,
    "reports"
)

# ==========================================
# Camera Configuration
# ==========================================

CAMERA_INDEX = 0

FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# ==========================================
# Face Recognition Configuration
# ==========================================

FACE_CONFIDENCE_THRESHOLD = 65

# ==========================================
# Eye Monitoring Configuration
# ==========================================

EAR_THRESHOLD = 0.20

CONSECUTIVE_FRAMES = 15

# ==========================================
# Application Configuration
# ==========================================

WINDOW_NAME = "Eagle_Vision_AI"

FONT = "FONT_HERSHEY_SIMPLEX"

# ==========================================
# Debug Information
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print("Eagle_Vision_AI Configuration")
    print("=" * 50)

    print(f"BASE_DIR                 : {BASE_DIR}")
    print(f"DATABASE_PATH            : {DATABASE_PATH}")
    print(f"MODEL_DIR                : {MODEL_DIR}")
    print(f"FACE_RECOGNIZER_MODEL    : {FACE_RECOGNIZER_MODEL}")
    print(f"FACE_CASCADE_PATH        : {FACE_CASCADE_PATH}")
    print(f"DATASET_DIR              : {DATASET_DIR}")
    print(f"LOG_DIR                  : {LOG_DIR}")
    print(f"REPORT_DIR               : {REPORT_DIR}")

    print("\n----- Camera Settings -----")
    print(f"CAMERA_INDEX             : {CAMERA_INDEX}")
    print(f"FRAME_WIDTH              : {FRAME_WIDTH}")
    print(f"FRAME_HEIGHT             : {FRAME_HEIGHT}")

    print("\n----- Face Recognition -----")
    print(f"FACE_CONFIDENCE_THRESHOLD: {FACE_CONFIDENCE_THRESHOLD}")

    print("\n----- Eye Monitoring -----")
    print(f"EAR_THRESHOLD            : {EAR_THRESHOLD}")
    print(f"CONSECUTIVE_FRAMES       : {CONSECUTIVE_FRAMES}")

    print("\n----- Application -----")
    print(f"WINDOW_NAME              : {WINDOW_NAME}")

    print("\nConfiguration Loaded Successfully.")