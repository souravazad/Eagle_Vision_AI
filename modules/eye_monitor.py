import cv2
import mediapipe as mp
import math



# ==========================================
# EAR Calculation
# ==========================================

def eye_aspect_ratio(points):

    A = math.dist(
        points[1],
        points[5]
    )


    B = math.dist(
        points[2],
        points[4]
    )


    C = math.dist(
        points[0],
        points[3]
    )


    ear = (A + B) / (2.0 * C)


    return ear




# ==========================================
# MediaPipe Face Mesh
# ==========================================

mp_face_mesh = mp.solutions.face_mesh


face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)



# ==========================================
# Eye Landmark Points
# ==========================================

LEFT_EYE = [

    33,
    160,
    158,
    133,
    153,
    144

]


RIGHT_EYE = [

    362,
    385,
    387,
    263,
    373,
    380

]




# ==========================================
# Variables
# ==========================================

EAR_THRESHOLD = 0.20


blink_count = 0


eye_closed = False


closed_frames = 0


DROWSY_LIMIT = 30





# ==========================================
# Eye Monitoring Function
# ==========================================

def monitor_eye(frame):

    global blink_count
    global eye_closed
    global closed_frames



    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )



    result = face_mesh.process(
        rgb
    )



    if not result.multi_face_landmarks:


        return {

            "EAR":0,
            "blink_count":blink_count,
            "drowsy":False

        }




    face = result.multi_face_landmarks[0]



    h, w, _ = frame.shape




    # ------------------------------
    # Left Eye
    # ------------------------------

    left_points=[]



    for id in LEFT_EYE:


        landmark = face.landmark[id]


        x = int(
            landmark.x*w
        )


        y = int(
            landmark.y*h
        )


        left_points.append(
            (x,y)
        )




    # ------------------------------
    # Right Eye
    # ------------------------------

    right_points=[]



    for id in RIGHT_EYE:


        landmark = face.landmark[id]


        x=int(
            landmark.x*w
        )


        y=int(
            landmark.y*h
        )


        right_points.append(
            (x,y)
        )




    left_EAR = eye_aspect_ratio(
        left_points
    )


    right_EAR = eye_aspect_ratio(
        right_points
    )



    avg_EAR = (
        left_EAR + right_EAR
    ) / 2





    # ------------------------------
    # Blink Detection
    # ------------------------------

    if avg_EAR < EAR_THRESHOLD:


        closed_frames += 1


        eye_closed = True



    else:


        if eye_closed:


            blink_count += 1


        eye_closed = False


        closed_frames = 0





    # ------------------------------
    # Drowsiness
    # ------------------------------

    if closed_frames > DROWSY_LIMIT:

        drowsy = True

    else:

        drowsy = False





    return {

        "EAR":round(avg_EAR,2),

        "blink_count":blink_count,

        "drowsy":drowsy

    }