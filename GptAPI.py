import openai
import requests

# OpenAI API 키 설정
openai.api_key = ""

# ChatGPT API 호출 및 응답 전송 함수
def send_diary_entry():
    response = openai.ChatCompletion.create(
        model="gpt-4.0-mini",  # 원하는 모델 선택
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "사용자의 활동 데이터와 피부 데이터를 기반으로 오늘의 피부 상태와 활동에 따른 일지를 작성해줘."}  # 원하는 메시지 추가
        ]
    )

    # 응답 결과를 가져옴
    diary_content = response['choices'][0]['message']['content']

    # 전송할 URL 설정 (result/diary로 전송)
    url = "http://your-server.com/result/diary"  # 실제 URL로 변경 필요

    # 전송할 데이터
    data = {
        'diary_entry': diary_content
    }

    # POST 요청을 통해 URL로 데이터 전송
    response = requests.post(url, json=data)

    # 전송 성공 여부 확인
    if response.status_code == 200:
        print("일지가 성공적으로 전송되었습니다!")
    else:
        print(f"전송 실패: {response.status_code}, {response.text}")

# 일지 생성 및 전송 함수 호출
send_diary_entry()
