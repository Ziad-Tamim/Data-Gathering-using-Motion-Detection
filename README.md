# Webcam Data Gatherer using Motion Detection
date: 06/04/2024
## Description
This Python script utilizes OpenCV to gather data from a webcam, focusing specifically on detecting motion. It initializes the webcam, captures video data, and uses frame differencing to detect movement. When movement is detected, the video is recorded for a specified duration. This tool is ideal for surveillance or monitoring environments where capturing movement is necessary.

## How to Use
### Prerequisites
* Python 3.x
* OpenCV library installed (cv2)
### Steps
1. Ensure Python and OpenCV are correctly installed on your system.
2. Save the script in a file, for example, motion_detector.py.
3. Open a terminal or command prompt.
4. Run the script by typing python motion_detector.py.
5. The script will start capturing video from the default webcam. Movement in front of the camera will trigger recording.
6. Press 'ESC' to exit the script.
### Changeable Variables
* Camera Index: cap = cv2.VideoCapture(1) - The index specifies which camera to use. 0 is usually the default camera. Change the index if you have multiple cameras or the default does not work.
* Resolution: cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) and cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360) - These lines set the resolution of the video capture. You can adjust these values according to your webcam's supported resolutions.
* Recording Duration: record_duration = 20 - Specifies how long (in seconds) the script should record after detecting movement. Adjust this value based on your needs.
* Movement Threshold: threshold=1000 in is_movement_detected function - This value determines the minimum size of detected movement to consider as valid. Increase or decrease this value to make movement detection more or less sensitive.
## Other
### Code Structure
* initialize_capture(): Initializes webcam capture with improved resolution settings.
* get_frame_difference(frame1, frame2): Calculates the difference between two consecutive frames to detect movement.
* is_movement_detected(contours, threshold=1000): Determines if the detected movement exceeds a certain size threshold.
* main(): Main function that orchestrates the capture, detection, and recording process.
### Troubleshooting
* If the script does not access your webcam, try changing the camera index in cv2.VideoCapture(1).
* Ensure the specified resolution matches your webcam's capabilities. Mismatched resolutions may result in errors or suboptimal video quality.
