from flask import Flask, render_template, request, jsonify
from PIL import Image
import os
import oracledb
import http.client
import io

app = Flask(__name__)

# RapidAPI 설정
RAPIDAPI_HOST = "skin-analyze-pro.p.rapidapi.com"
RAPIDAPI_KEY = "a50fd6368dmsh86f6cbea142ed97p17f40djsneb900fa6f6ba"

@app.route('/')
def main():
    return render_template('main.html')
@app.route('/result/<result_type>', methods=['GET', 'POST'])
def index(result_type):
    if str(result_type) == 'activity':
        activity = {'laundry': 0
            , 'dish': 1
            , 'vacuum': 1
            , 'sleep_num': 6.88
            , 'sleep_qual_awake': 0.39
            , 'sleep_qual_rem': 1.85
            , 'sleep_qual_core': 2.68
            , 'sleep_qual_deep': 1.94
            , 'steps': 12116
            , 'leisure_index': 0.80}
        if 0.81 <= activity['leisure_index'] <= 1.0:
            activity['leisure'] = '매우 좋음'
            activity['aff'] = 5
        elif 0.61 <= activity['leisure_index'] <= 0.8:
            activity['leisure'] = '좋음'
            activity['aff'] = 4
        elif 0.41 <= activity['leisure_index'] <= 0.6:
            activity['leisure'] = '보통'
            activity['aff'] = 3
        elif 0.21 <= activity['leisure_index'] <= 0.4:
            activity['leisure'] = '나쁨'
            activity['aff'] = 2
        else:
            activity['leisure'] = '매우 나쁨'
            activity['aff'] = 1
        return render_template('activity.html', data=activity)
    elif str(result_type) == 'diary':
        return render_template('diary.html')
    else:
        activity = {'laundry': 0
            , 'dish': 1
            , 'vacuum': 1
            , 'sleep_num': 6.88
            , 'sleep_qual_awake': 0.39
            , 'sleep_qual_rem': 1.85
            , 'sleep_qual_core': 2.68
            , 'sleep_qual_deep': 1.94
            , 'steps': 12116
            , 'leisure_index': 0.80}
        if 0.81 <= activity['leisure_index'] <= 1.0:
            activity['leisure'] = '매우 좋음'
            activity['aff'] = 5
        elif 0.61 <= activity['leisure_index'] <= 0.8:
            activity['leisure'] = '좋음'
            activity['aff'] = 4
        elif 0.41 <= activity['leisure_index'] <= 0.6:
            activity['leisure'] = '보통'
            activity['aff'] = 3
        elif 0.21 <= activity['leisure_index'] <= 0.4:
            activity['leisure'] = '나쁨'
            activity['aff'] = 2
        else:
            activity['leisure'] = '매우 나쁨'
            activity['aff'] = 1
        if request.method == 'POST':
            path = './static/images/'
            file = request.files['file']

            # 이미지 저장
            file_path = os.path.join(path, file.filename)
            file.save(file_path)

            return render_template('skin.html', data=activity)
        return render_template('skin.html', data=activity)


# Oracle Instant Client 설치 경로 설정 (Thick 모드 활성화)
# 현재 우리 버전은 11.2.x 여서 thin 모드로 실행이 안된다. 버전이 낮아서,,,
oracledb.init_oracle_client(lib_dir="C:/instantclient_19_24")  # Windows의 경우

# Oracle DB 연결 정보
def get_db_connection():
    connection = oracledb.connect(
        user='hrd',            # 사용자 이름
        password='1234',       # 비밀번호
        dsn='localhost/XE' # 호스트:포트/서비스명
    )
    return connection


# 네이버회원 테이블의 모든 데이터를 조회하는 함수
def fetch_all_naver_members():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # SQL 쿼리 실행: 네이버회원 테이블의 모든 데이터 가져오기
        cursor.execute("SELECT * FROM 네이버회원")

        # 결과 가져오기
        rows = cursor.fetchall()

        # 가져온 데이터를 출력
        for row in rows:
            print(row)

    except oracledb.DatabaseError as e:
        print(f"데이터 조회 실패: {e}")
    finally:
        # 커서와 연결 닫기
        cursor.close()
        connection.close()


# # DB 연결 및 데이터 조회 테스트
# try:
#     conn = get_db_connection()
#     print("Oracle DB 연결 성공")
#
#     # 네이버회원 테이블의 모든 데이터 가져오기
#     fetch_all_naver_members()
#
#     conn.close()
# except oracledb.DatabaseError as e:
#     print(f"Oracle DB 연결 실패: {e}")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)