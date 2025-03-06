import numpy as np
from PIL import Image
import mediapipe as mp
from config import IMAGE_PATH

# Khởi tạo MediaPipe Pose
mp_pose = mp.solutions.pose
human_detection = mp_pose.Pose()

def detect_pose():
    """Nhận diện người trong ảnh."""
    try:
        image = Image.open(IMAGE_PATH).convert("RGB")
        image_np = np.array(image)

        results = human_detection.process(image_np)
        return bool(results.pose_landmarks)  # Trả về True nếu có người
    except Exception as e:
        print(f"⚠️ Lỗi nhận diện tư thế: {e}")
        return False
