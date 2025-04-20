import face_recognition
import pickle

def encode_faces(image_folder):
    encodings = []
    # Load images, encode faces...
    with open('encodings.pickle', 'wb') as f:
        pickle.dump(encodings, f)