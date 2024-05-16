import sys
import time

import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils

model = 'ssd_mobilenet_v2_metadata.tflite'
cameraId = 0
width = 640
height = 480
num_threads = 4
enable_edgetpu = False

# Start capturing video input from the camera
cap = cv2.VideoCapture(cameraId)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Initialize the object detection model
base_options = core.BaseOptions(
  file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)
detection_options = processor.DetectionOptions(
  max_results=100, score_threshold=0.5)
options = vision.ObjectDetectorOptions(
    base_options=base_options, detection_options=detection_options)
detector = vision.ObjectDetector.create_from_options(options)

def count(interval):
    # Continuously capture images from the camera and run inference
    global cap, detector
    
    # Variables to calculate FPS
    counter, fps = 0, 0
    start_time = round(time.time())

    # Visualization parameters
    row_size = 20  # pixels
    left_margin = 24  # pixels
    text_color = (0, 0, 255)  # red
    font_size = 1
    font_thickness = 1
    fps_avg_frame_count = 10

    last_camera_open_time = time.time()
    Maxjumlah = 0
    while True:
        current_time = round(time.time())
        #Reopen the camera every 30 seconds
        if current_time - last_camera_open_time < interval:
            if 'cap' in locals():
                cap.release()

            # cap = cv2.VideoCapture(0)
            # cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            # cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

        success, image = cap.read()
        if not success:
            sys.exit(
                'ERROR: Unable to read from webcam. Please verify your webcam settings.'
            )

        counter += 1
        image = cv2.flip(image, 1)

        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Create a TensorImage object from the RGB image.
        input_tensor = vision.TensorImage.create_from_array(rgb_image)

        # Run object detection estimation using the model.
        detection_result = detector.detect(input_tensor)
        jumlahIkan = len(detection_result.detections)
        if jumlahIkan > Maxjumlah:
            Maxjumlah = jumlahIkan

        # Draw keypoints and edges on input image
        image = utils.visualize(image, detection_result)

        # Calculate the FPS
        if counter % fps_avg_frame_count == 0:
            end_time = time.time()
            fps = fps_avg_frame_count / (end_time - start_time)
            start_time = time.time()

        # Show the FPS
        fps_text = 'FPS = {:.1f}'.format(fps)
        text_location = (left_margin, row_size)
        cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                    font_size, text_color, font_thickness)
        
        # Show the number of detected fish
        jumlahIkan_text = 'Jumlah Ikan = {}'.format(jumlahIkan)
        jumlahIkan_location = (left_margin, row_size * 2)
        cv2.putText(image, jumlahIkan_text, jumlahIkan_location, cv2.FONT_HERSHEY_PLAIN,
                    font_size, text_color, font_thickness)

        # Stop the program if the ESC key is pressed.
        if cv2.waitKey(1) == 27:
            break
        cv2.imshow('object_detector', image)
    
    print("Jumlah ikan yang tedeteksi: {}".format(Maxjumlah))
    return Maxjumlah

def stopProgram():
    cap.release()
    cv2.destroyAllWindows()