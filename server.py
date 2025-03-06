import requests
from config import URL_SERVER

def update_status(new_status):
    """Gửi trạng thái 'yes' hoặc 'no' đến server."""
    data = {"status": new_status}
    print(f"🔄 Cập nhật trạng thái: {new_status}")

    try:
        response = requests.post(URL_SERVER, json=data)
        if response.status_code == 200:
            print("✅ Trạng thái cập nhật:", response.json())
        else:
            print("❌ Lỗi cập nhật trạng thái:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Lỗi khi gửi request: {e}")
