import subprocess
import os
from config import RTSP_URL, IMAGE_PATH

def capture_frame():
    """Chụp ảnh từ camera RTSP và lưu vào IMAGE_PATH."""
    print("📡 Đang chụp ảnh từ camera...")

    command = [
        "ffmpeg", "-rtsp_transport", "tcp", "-i", RTSP_URL,
        "-frames:v", "1", "-q:v", "2", IMAGE_PATH, "-y"
    ]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0 and os.path.exists(IMAGE_PATH):
            print("📸 Ảnh đã được lưu!")
            return True
        else:
            print("❌ Lỗi khi chụp ảnh từ RTSP!", result.stderr.decode())
            return False
    except Exception as e:
        print(f"⚠️ Lỗi khi gọi FFmpeg: {e}")
        return False
