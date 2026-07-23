"""
=========================================================
Eagle_Vision_AI v2.0
Module : InsightFace Engine
Author : Sourav Kumar Azad
=========================================================
"""

from insightface.app import FaceAnalysis

# ==========================================
# Initialize InsightFace
# ==========================================

print("=" * 60)
print("Initializing InsightFace Engine...")
print("=" * 60)

face_app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"]
)

face_app.prepare(
    ctx_id=0,
    det_size=(640, 640)
)

print("InsightFace Engine Ready.")
print("=" * 60)