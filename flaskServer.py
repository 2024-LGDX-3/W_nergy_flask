from flask import Flask, request, redirect
import requests
import json

from flask import Flask, request, jsonify
from flask_cors import CORS
import http.client

app = Flask(__name__)

# CORS 설정 (localhost:8081에서만 허용)
CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})

# RapidAPI 설정
RAPIDAPI_HOST = "skin-analyze-pro.p.rapidapi.com"
RAPIDAPI_KEY = "a50fd6368dmsh86f6cbea142ed97p17f40djsneb900fa6f6ba"


@app.route('/analyze', methods=['POST'])
def analyze():
    # 요청에서 파일을 받음
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    # 파일이 제대로 업로드되었을 때 처리
    if file:
        # 파일을 바이너리로 읽음
        image_data = file.read()

        # RapidAPI로 파일 전송
        boundary = '---011000010111000001101001'
        payload = (
                      f'--{boundary}\r\n'
                      'Content-Disposition: form-data; name="image"; filename="imagetest.jpg"\r\n'
                      'Content-Type: image/jpeg\r\n\r\n'
                  ).encode('utf-8') + image_data + f'\r\n--{boundary}--\r\n'.encode('utf-8')

        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': RAPIDAPI_HOST,
            'Content-Type': f"multipart/form-data; boundary={boundary}"
        }

        conn = http.client.HTTPSConnection(RAPIDAPI_HOST)
        conn.request("POST", "/facebody/analysis/skinanalyze-pro", payload, headers)

        res = conn.getresponse()
        data = res.read()

        # RapidAPI의 응답을 반환
        return jsonify({'message': 'File successfully uploaded and processed', 'response': data.decode("utf-8")}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


# img = Image.open(file_path)
# img = img.resize((500, 500))
#
# # 이미지를 메모리상에서 파일처럼 다룰 수 있도록 BytesIO 객체로 변환
# img_io = io.BytesIO()
# img.save(img_io, format='JPEG')  # 이미지를 JPEG 형식으로 저장
# img_io.seek(0)  # 파일 포인터를 처음으로 이동
#
# # 파일이 제대로 업로드되었을 때 처리
# if img:
#     # 파일을 바이너리로 읽음
#     image_data = img_io.read()
#
#     # RapidAPI로 파일 전송
#     boundary = '---011000010111000001101001'
#     payload = (
#                   f'--{boundary}\r\n'
#                   'Content-Disposition: form-data; name="image"; filename="imagetest.jpg"\r\n'
#                   'Content-Type: image/jpeg\r\n\r\n'
#               ).encode('utf-8') + image_data + f'\r\n--{boundary}--\r\n'.encode('utf-8')
#
#     headers = {
#         'x-rapidapi-key': RAPIDAPI_KEY,
#         'x-rapidapi-host': RAPIDAPI_HOST,
#         'Content-Type': f"multipart/form-data; boundary={boundary}"
#     }
#
#     conn = http.client.HTTPSConnection(RAPIDAPI_HOST)
#     conn.request("POST", "/facebody/analysis/skinanalyze-pro", payload, headers)
#
#     res = conn.getresponse()
#     data = res.read().decode("utf-8")
#     # 응답 데이터를 변수에 담아 템플릿으로 전달
#     response_data = {
#         'message': 'File successfully uploaded and processed',
#         'response': data
#     }
#     print('response_data:', response_data)
#     # RapidAPI의 응답을 반환