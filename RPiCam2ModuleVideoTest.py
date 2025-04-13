import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

# Initialize the camera
picam2 = Picamera2()

# Configure the camera
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Start the camera
picam2.start()
print("Camera started successfully!")

# Wait for camera to warm up
time.sleep(2)

# Simple video filename
video_path = "test_video.mp4"

# Create an encoder for video recording
encoder = H264Encoder(bitrate=10000000)

print(f"Recording video to {video_path}...")
picam2.start_recording(encoder, video_path)

# Show a countdown during recording
for i in range(10, 0, -1):
    print(f"Recording: {i} seconds remaining...")
    time.sleep(1)

picam2.stop_recording()
print(f"Video recording completed and saved as {video_path}")

# Close the camera
picam2.close()
print("Camera test completed successfully!")