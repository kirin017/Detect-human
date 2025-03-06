

1. Giới Thiệu

Chương trình này sử dụng ffmpeg để chụp ảnh từ luồng RTSP của camera, sau đó sử dụng thư viện Mediapipe để phát hiện người và gửi trạng thái đến một server Flask.

2. Cấu Trúc Dự Án

/detect-human\
│── main.py                 Chạy chương trình chính \
│── config.py               Chứa cấu hình (RTSP, server URL)\
│── capture.py              Chụp ảnh từ RTSP\
│── detection.py            Nhận diện người với MediaPipe\
│── server.py               Gửi trạng thái đến server\
│── requirements.txt        Danh sách thư viện cần cài đặt    \           

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

Cập nhật biến RTSP_URL với đường dẫn luồng RTSP trong config.py:\
RTSP_URL = "YOUR_URL"\
URL_SERVER = "SERVER_URL"\
d. Chạy chương trình

python main.py \
Chương trình sẽ post đến server trạng thái của camera có phát hiện người hay không. \
server sẽ nhận yes nếu camera phát hiện người và no nếu không phát hiện.\
4. Mở rộng

Đảm bảo ffmpeg đã được cài đặt và có thể chạy từ terminal.

Kiểm tra đường dẫn RTSP có chính xác không.

Có thể mở rộng các phương pháp nhận diện khác bằng cách thay đổi mô hình trong detect.py


