from flask import Flask, request, jsonify, send_from_directory
import subprocess
import threading
import json
import importlib.metadata

from screen_ocr import stop_recording

app = Flask(__name__)
process = None

# Function to install missing packages based on requirements.json
def setup_environment():
    with open('requirements.json', 'r') as file:
        requirements = json.load(file)
        required_packages = requirements.get("dependencies", [])
        
        installed_packages = {pkg for pkg in importlib.metadata.distributions()}
        missing_packages = [pkg for pkg in required_packages if pkg not in installed_packages]
        
        if missing_packages:
            print(f"Missing packages found: {missing_packages}")
            subprocess.call(['pip', 'install', *missing_packages])
        else:
            print("All required packages are already installed.")

# Function to fetch and run the Python script specified in the separate JSON file
def run_screen_recorder(interval, duration):
    global process
    command = f"python screen_ocr.py {interval} {duration}"
    process = subprocess.Popen(command, shell=True)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/start', methods=['POST'])
def start():
    data = request.json
    interval = data.get('interval')
    duration = data.get('duration')

    # Validate input
    if interval is None or duration is None:
        return jsonify({"message": "Interval and duration must be provided."}), 400

    # Set up environment if not already done
    setup_thread = threading.Thread(target=setup_environment)
    setup_thread.start()
    setup_thread.join()

    # Start the screen recorder
    recorder_thread = threading.Thread(target=run_screen_recorder, args=(interval, duration))
    recorder_thread.start()

    return jsonify({"message": "Screen recorder started."})

@app.route('/stop', methods=['POST'])
def stop():
    global process
    # Stop the screen recording by changing the flag
    stop_recording()  # Ensure the flag in screen_ocr.py is set to False
    if process:
        process.terminate()
        process = None
        return jsonify({"message": "Screen recorder stopped."})
    return jsonify({"message": "No screen recorder is running."})


if __name__ == "__main__":
    app.run(debug=True)
