# Student Performance Analyzer

Ứng dụng web giúp phân tích dữ liệu học sinh từ file Excel bằng **Flask**, **Pandas** và **Google Gemini API**.  
Người dùng có thể tải lên file Excel, hệ thống sẽ phân tích và đưa ra:  

- Danh sách học sinh có nguy cơ bỏ học  
- Tỷ lệ rủi ro (%)  
- Nguyên nhân chính (dựa trên điểm số)  
- Đề xuất cải thiện  

---

## Tính năng chính
- Upload file Excel (.xlsx, .xls)  
- Tự động phân tích dữ liệu bằng **Gemini 2.5 Pro**  
- Hiển thị kết quả phân tích rõ ràng  
- Cho phép **lưu kết quả** phân tích về máy (.txt)  

---

## 🛠️ Cài đặt

### 1. Clone repo
```bash
git clone https://github.com/yourusername/student-performance-analyzer.git
cd student-performance-analyzer
```

---

## Tạo môi trường ảo (khuyến nghị)
```bash
python -m venv venv
source venv/bin/activate   # MacOS/Linux
venv\Scripts\activate      # Windows
```

---

## Cài dependencies
```bash
pip install -r requirements.txt
```

---

## Lấy API key
- truy cập Google AI Studio để lấy key

---

## Chạy ứng dụng
```bash
python app.py
```
- truy cập http://127.0.0.1:5000

---

## Cách sử dụng
- Mở ứng dụng trên trình duyệt.
- Tải lên file Excel chứa dữ liệu học sinh.
- Nhấn Phân tích để hệ thống xử lý và hiển thị kết quả.
- Nhấn Lưu kết quả để tải kết quả về máy.

---

## Cấu trúc thư mục
```bash
project/
│── app.py              # Flask backend
│── requirements.txt    # Thư viện cần thiết
│── index.html          # Giao diện frontend
│── uploads/            # Nơi lưu file Excel đã upload
```
