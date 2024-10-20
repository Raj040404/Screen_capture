# Screen Recorder Application

This project is a web-based screen recording tool that allows users to start and stop screen recordings based on specific time intervals and durations. The application consists of a front-end interface built with HTML, CSS, and JavaScript, and a back-end server developed using Flask. It also includes a Python script for capturing screenshots at defined intervals.

## Features

- Simple and intuitive UI for setting interval and duration for screen recording.
- Button controls to start and stop the screen recording.
- Automatically installs required dependencies.
- The backend is developed using Flask, and the screen recording logic is implemented in Python.

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.6+
- Pip (Python package manager)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/screenshot-capture.git
   cd screenshot-capture

Install the required Python packages:


pip install -r requirements.txt
Verify that requirements.json lists all necessary dependencies:

json

{
  "dependencies": [
    "flask",
    "pillow"
  ]
}
Add the following in script_config.json to specify the script name:

json

{
  "script": "screen_ocr.py"
}
Usage
Running the Application
Start the Flask server:


python app.py
The server will run at http://127.0.0.1:5000.

Open a web browser and navigate to http://127.0.0.1:5000. You will see the screen recorder interface.

##Front-End UI

Set the interval (in seconds) for how often screenshots should be taken.
Specify the duration in minutes and seconds.
Click the "Start Recording" button to begin the screen recording.
Click the "Stop Recording" button to stop the recording process.
Stopping the Server
Press CTRL+C in the terminal to stop the Flask server.

##How It Works

The front-end sends a POST request to /start on the server, with the specified interval and duration.
The Flask backend reads this input, installs any missing dependencies, and launches the screen_ocr.py script.
The script captures screenshots at the defined interval until the total duration is reached.
The Stop Recording button sends a request to terminate the process.
Sample JSON File: requirements.json
json

{
  "dependencies": [
    "flask",
    "pillow"
  ]
}

##Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Screen Recording: Python (using libraries like Pillow)
Troubleshooting
Interval and Duration Not Received: Ensure you are filling out all input fields in the web interface.
Script Keeps Running: Ensure the screen_ocr.py can be terminated correctly by the Stop Recording button.
Dependency Warnings: If a deprecation warning about pkg_resources appears, consider updating your dependencies.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch-name).
Make your changes and commit them (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch-name).
Create a new Pull Request.

##License

This project is licensed under the MIT License. See the LICENSE file for details.

##Acknowledgements

Special thanks to the developers of Flask and Python libraries.

