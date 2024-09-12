from flask import Flask, jsonify, render_template
import oracledb

app = Flask(__name__)

# Oracle DB 연결 정보
def get_db_connection():
    connection = oracledb.connect(
        user='hrd',      # 사용자 이름
        password='1234',  # 비밀번호
        dsn='localhost:1521/xe'  # 호스트:포트/서비스명
    )
    return connection

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/data', methods=['GET'])
def get_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # SQL 쿼리 실행
    cursor.execute("SELECT * FROM TB_EMP")  # 원하는 테이블명으로 수정
    rows = cursor.fetchall()
    
    # 커서와 연결 종료
    cursor.close()
    connection.close()

    # 결과를 JSON 형식으로 반환
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
