import cv2

# img = cv2.imread("Resources/logo.png")

# cv2.imshow("Output", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture("Resources/test.mp4")

# while True:
#     sucess,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Create a VideoCapture object to access the webcam (0 represents the default webcam)

cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the captured frame
    cv2.imshow('Webcam', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
