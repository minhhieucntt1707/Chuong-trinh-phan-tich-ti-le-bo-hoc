from flask import Flask, render_template, request, jsonify
import pandas as pd
import google.generativeai as genai
import os

# === CONFIGURE GEMINI ===
genai.configure(api_key="AIzaSyBl2L5lJ2_eFH6SQo6DNjTIJ2XD5bhT7Fw")
model = genai.GenerativeModel("gemini-2.5-pro")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        df = pd.read_excel(filepath)
        prompt = f"""
Bạn là chuyên gia phân tích giáo dục. Hãy trình bày kết quả phân tích dữ liệu học sinh sau theo định dạng rõ ràng:

- **Danh sách học sinh có nguy cơ bỏ học**
- **Tỷ lệ rủi ro (%)**
- **Nguyên nhân chính (ghi rõ điểm số gây ra nguyên nhân)**
- **Đề xuất cải thiện**

Dữ liệu mẫu:
{df.head(10).to_string(index=False)}

Trình bày kết quả bằng các tiêu đề rõ ràng, gạch đầu dòng, và ngắn gọn.
"""
        response = model.generate_content(prompt)
        return jsonify({'analysis': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
