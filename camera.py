import face_recognition
import cv2 as cv
import Data.person as DataBase

video_capture = cv.VideoCapture(0)
#video_capture = cv2.VideoCapture(0)
process_this_frame = True

def testCamera():
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        # Display the resulting image
        cv.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


"""
    Got a lot of help from the face_recognititon 
    examples for this function.
    URL: https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py
"""

def DrawfaceBoxTest1():
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()

        small_frame = cv.resize(frame, (0,0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_Stat_Name_location = checkfaces(face_encodings, face_locations)
        
        process_this_frame = not process_this_frame

        print("face_status_name_location: " + str(face_Stat_Name_location))
        
        for face in face_Stat_Name_location:
            top = (face[2])[0] * 4 
            right = (face[2])[1] * 4
            bottom = (face[2])[2] * 4
            left = (face[2])[3] * 4

            if(face[1] == 'Owner'):
                #green
                Color = (0, 255, 0)
            elif(face[1] == 'Friend'):
                #Blue
                Color = (255, 0, 0)
            else:
                #red
                Color = (0, 0, 255)

            cv.rectangle(frame, (left, top), (right, bottom), Color, 2)

            cv.rectangle(frame, (left, bottom - 35), (right, bottom), Color, cv.FILLED)
            font = cv.FONT_HERSHEY_DUPLEX
            cv.putText(frame, face[0], (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv.waitKey(5) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv.destroyAllWindows()
        


def checkfaces(faces, locations):
    face_Stat_Name_location = []
    check = True
    for face in range(len(faces)):
        for person in DataBase.Master:
            match = face_recognition.compare_faces(person.encode, faces[face])
            print(match)
            if True in match:
                face_Stat_Name_location.append([person.name, person.status, locations[face]])
                check = False
                break

        #face not found
        if(check):
            face_Stat_Name_location.append(["UNKNOWN", "Enemy", locations[face]])
        check = True

    return face_Stat_Name_location


                

