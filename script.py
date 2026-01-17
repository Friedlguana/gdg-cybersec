import os
import cv2

valid_extensions = ('.png')
image_files = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
detector = cv2.QRCodeDetector()

print(f"Scanning {len(image_files)} files... (All results will be saved)\n")

with open("decode.txt", "w") as f:
    for filename in image_files:
        img = cv2.imread(filename)
        if img is None:
            continue

        # Detect and decode the QR code
        data, bbox, _ = detector.detectAndDecode(img)

        if data:
            print(f"Decoded data from {filename}: {data}")
            f.write(f"[{filename}]: {data}\n")

print("\nScan complete. Check decode.txt for all decoded results.")
