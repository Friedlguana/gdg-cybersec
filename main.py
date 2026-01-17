import os
import cv2

# Phrases to ignore
decoys = [
    "decoy", "another one", "no flag", "keep moving", 
    "wrong code", "still not", "move along", "nothing useful", 
    "continue searching", "empty path"
]

valid_extensions = ('.png')
image_files = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
detector = cv2.QRCodeDetector()

print(f"Scanning {len(image_files)} files... (Filtering decoys)\n")

with open("decode.txt", "w") as f:
    for filename in image_files:
        img = cv2.imread(filename)
        if img is None:
            continue

        data, bbox, _ = detector.detectAndDecode(img)

        if data:
            if not any(phrase in data.lower() for phrase in decoys):
                print(f"!!! POSSIBLE FLAG FOUND in {filename} !!!")
                print(f"Data: {data}\n")
                f.write(f"POTENTIAL FLAG [{filename}]: {data}\n")
            else:
                print(".", end="", flush=True)

print("\nScan complete. Check decode.txt for any potential flags.")
