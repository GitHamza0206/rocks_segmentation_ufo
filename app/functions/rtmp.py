import cv2
import numpy as np

# URL of the RTMP stream
stream_url = "rtmp://185.192.96.228/live/livestream?secret=b7a0e01073b6448785799d4dd79a1dd4"

# Open the RTMP stream
cap = cv2.VideoCapture(stream_url)

# Check if the stream is opened successfully
if not cap.isOpened():
    print("Error: Could not open stream.")
    exit()

# Read and display the stream frames with edge detection
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Convert edges to BGR (3 channels) to concatenate with the original frame
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Concatenate the original frame and the edge-detected frame horizontally
    combined = np.hstack((frame, edges_bgr))

    # Display the combined image
    cv2.imshow('Original and Edge Detection', combined)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the stream and close the display window
cap.release()
cv2.destroyAllWindows()
