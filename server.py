import oracledb

# Oracle Instant Client 설치 경로 설정 (Thick 모드 활성화)
# 현재 우리 버전은 11.2.x 여서 thin 모드로 실행이 안된다. 버전이 낮아서,,,
oracledb.init_oracle_client(lib_dir="C:/instantclient_19_24")  # Windows의 경우

# Oracle DB 연결 정보
def get_db_connection():
    connection = oracledb.connect(
        user='hrd',            # 사용자 이름
        password='12345',       # 비밀번호
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


# DB 연결 및 데이터 조회 테스트
try:
    conn = get_db_connection()
    print("Oracle DB 연결 성공")

    # 네이버회원 테이블의 모든 데이터 가져오기
    fetch_all_naver_members()

    conn.close()
except oracledb.DatabaseError as e:
    print(f"Oracle DB 연결 실패: {e}")
