import asyncio
import os
from capture import capture_frame
from detection import detect_pose
from server import update_status
from config import IMAGE_PATH

async def main():
    """Vòng lặp chính."""
    while True:
        captured = capture_frame()
        if captured and os.path.exists(IMAGE_PATH):
            status = detect_pose()
            update_status("yes" if status else "no")
            await asyncio.sleep(4 if status else 2)  # Nếu có người: chờ 4s, không có: chờ 2s

if __name__ == "__main__":
    asyncio.run(main())
