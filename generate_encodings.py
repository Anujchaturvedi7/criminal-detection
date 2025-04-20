import os
import face_recognition
import pickle
from tqdm import tqdm

DATASET_DIR = "augmented_dataset"
ENCODINGS_PATH = "face_encodings.pkl"

known_encodings = []
known_names = []

for root, dirs, files in os.walk(DATASET_DIR):
    for file in tqdm(files):
        if file.endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(root, file)
            name = os.path.basename(root)  # folder name as identity

            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(name)

with open(ENCODINGS_PATH, "wb") as f:
    pickle.dump({"encodings": known_encodings, "names": known_names}, f)

print("[✔] Encodings saved in face_encodings.pkl")
