# Importing Package OpenCV
import cv2

# Read the video from specified location,
# replace your video file location with "video_path"
# or '0' for webcam stream
capture = cv2.VideoCapture("video_path")

# Initialize frame count to Zero
frame = 0

while True:
    # reading from frame
    bool_ret, image = capture.read()

    # Check if frames are correctly reading
    if not bool_ret:
        break

    else:
        # Enter a name to the image, replace img_name with your required name
        name = 'img_name' + str(frame) + '.jpg'
        # writing the extracted images
        print(name)
        cv2.imwrite(name, image)
        # increasing counter
        frame += 1

# Release capture class and destroy windows once video is complete.
capture.release()
cv2.destroyAllWindows()
