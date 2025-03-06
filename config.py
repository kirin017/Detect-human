import os

# URL RTSP của camera
RTSP_URL = "rtsp://your_camera_url"

# URL server Flask để cập nhật trạng thái
URL_SERVER = "http://localhost:5000/update_status"

# Đường dẫn lưu ảnh
IMAGE_PATH = os.path.join("frames", "frame.jpg")
