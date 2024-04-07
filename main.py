import cv2
import time

def initialize_capture():
    """Initialize the webcam and video writer with improved resolution."""
    cap = cv2.VideoCapture(1)  # 0 is typically the default webcam
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set the width to 1920 pixels
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)  # Set the height to 1080 pixels
    
    # Check if the resolution was set correctly
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"Set resolution: {actual_width} x {actual_height}")
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(actual_width), int(actual_height)))
    return cap, out


def get_frame_difference(frame1, frame2):
    """Calculate the difference between two frames."""
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def is_movement_detected(contours, threshold=1000):
    """Check if any movement is detected in the contours."""
    for contour in contours:
        if cv2.contourArea(contour) > threshold:
            return True
    return False

def main():
    cap, out = initialize_capture()
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    movement_detected_time = None  # Time when movement was last detected
    record_duration = 20  # Duration to record after detecting movement, in seconds

    try:
        while cap.isOpened():
            contours = get_frame_difference(frame1, frame2)
            current_time = time.time()
            
            if is_movement_detected(contours):
                movement_detected_time = current_time  # Update the time of last detected movement
                print("Movement detected!")  # Output message when movement is detected

            if movement_detected_time and (current_time - movement_detected_time <= record_duration):
                out.write(frame1)  # Write the frame if within record duration after movement
                # print("Recording...")  # Output message when recording

            cv2.imshow("feed", frame1)
            frame1 = frame2
            ret, frame2 = cap.read()

            if cv2.waitKey(40) == 27:  # Press 'ESC' to exit
                break
    except KeyboardInterrupt:
        pass
    finally:
        # Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
