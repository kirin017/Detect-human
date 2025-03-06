import mediapipe as mp
import numpy as np
from PIL import Image
import requests
import asyncio
import os

mp_pose = mp.solutions.pose  
human_detection = mp_pose.Pose()

import subprocess


RTSP_URL = ""
URL_SERVER = ""
IMAGE_PATH = os.path.join("frames", "frame.jpg")

async def capture_frame():
    """Chụp ảnh từ camera RTSP"""
    print("📡 Đang chụp ảnh từ camera...")
    command = [
        "ffmpeg", "-rtsp_transport", "tcp", "-i", RTSP_URL,
        "-frames:v", "1", "-q:v", "2", IMAGE_PATH, "-y"
    ]
    
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print("📸 Ảnh đã được lưu!")
        return True
    else:
        print("❌ Lỗi khi chụp ảnh từ RTSP!")
        return False



def update_status(new_status, URL_SERVER):
    url = URL_SERVER  # Đảm bảo rằng URL trỏ đến server Flask đang chạy
    data = {'status': new_status}
    print(data)
    try:
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            print("Trạng thái đã được cập nhật:", response.json())
        else:
            print("Lỗi cập nhật trạng thái:", response.json())
    except requests.exceptions.RequestException as e:
        print("Có lỗi xảy ra:", e)

async def detect_faces(image_path):
    """Nhận diện khuôn mặt từ ảnh"""
    try:
        image = Image.open(image_path).convert("RGB")
        image_np = np.array(image)

        results = human_detection.process(image_np)
        return bool(results.pose_landmarks) # True nếu phát hiện khuôn mặt
    except Exception as e:
        print(f"Lỗi nhận diện khuôn mặt: {e}")
        return False
async def main():
    
    while True:
        captured = await capture_frame()
        if captured and os.path.exists(IMAGE_PATH):
            print("Captured")
            status = await detect_faces(IMAGE_PATH)
            if status:
                update_status("yes")
                await asyncio.sleep(4)
            else:
                update_status("no")
                await asyncio.sleep(2) 
            update_status("no")
asyncio.run(main())