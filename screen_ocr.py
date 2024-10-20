import pyautogui
import time
import cv2
import numpy as np
import pytesseract
from PIL import Image
import os
import sys
import requests

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Flag to control the recording process
is_recording = 0  # Initialize to 0 (not recording)

def screen_record(duration=10, interval=1, output_folder="screenshots"):
    global is_recording
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    start_time = time.time()
    counter = 0
    
    # Start recording only if is_recording is 1
    while time.time() - start_time < duration and is_recording == 1:  # Check if recording is active
        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(output_folder, f"screenshot_{counter}.png"))
        counter += 1
        time.sleep(interval)

    print("Screen recording completed.")

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer "}

def query(folder="screenshots"):
    text = ""
    text2 = ""

    image_files = [f for f in os.listdir(folder) if f.endswith('.png')]
    
    for image_file in image_files:
        image_path = os.path.join(folder, image_file)
        text2 += extract_text_from_image(image_path)
        with open(image_path, "rb") as f:
            data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            text += str(response.json())
    return text, text2

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    extracted_text = pytesseract.image_to_string(image_cv)
    return extracted_text

def start_recording(duration, interval):
    global is_recording
    is_recording = 1  # Set the flag to allow recording
    screen_record(duration, interval)

def stop_recording():
    global is_recording
    is_recording = 0  # Set the flag to stop recording

if __name__ == "__main__":
    # Get interval and duration from command line arguments
    if len(sys.argv) != 3:
        print("Usage: python screen_ocr.py <interval> <duration>")
        sys.exit(1)

    interval = int(sys.argv[1])  # Get the interval from the command line
    duration = int(sys.argv[2])   # Get the duration from the command line

    try:
        start_recording(duration, interval)
        a = query()
        print(a)
    except Exception as e:
        print(f"Error: {e}")
        stop_recording()  # Ensure recording stops on error
