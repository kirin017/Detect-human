Hướng Dẫn Sử Dụng Mã Nguồn

1. Giới Thiệu

Chương trình này sử dụng ffmpeg để chụp ảnh từ luồng RTSP của camera, sau đó sử dụng thư viện Mediapipe để nhận diện khuôn mặt và gửi trạng thái đến một server Flask.

2. Cấu Trúc Dự Án

: Chụp ảnh từ camera RTSP và lưu vào thư mục frames.

: Gửi trạng thái nhận diện người (yes/no) đến một server Flask.

: Sử dụng Mediapipe để phát hiện người trong ảnh.

3. Hướng Dẫn Cài Đặt

a. Cài đặt thư viện cần thiết

Chạy lệnh sau để cài đặt các thư viện cần thiết:

pip install -r requirements.txt


b. Cài đặt ffmpeg

Đảm bảo rằng ffmpeg đã được cài đặt. Nếu chưa, hãy cài đặt theo hệ điều hành:

Windows: Tải từ https://ffmpeg.org/download.html và thêm vào system PATH.

Ubuntu:

sudo apt update && sudo apt install ffmpeg


c. Cấu hình RTSP và URL_SERVER

Cập nhật biến RTSP_URL với đường dẫn luồng RTSP :
RTSP_URL = "YOUR_URL"
URL_SERVER = "SERVER_URL"
d. Chạy chương trình

python app.py

4. Lưu Ý

Đảm bảo ffmpeg đã được cài đặt và có thể chạy từ terminal.

Kiểm tra đường dẫn RTSP có chính xác không.


