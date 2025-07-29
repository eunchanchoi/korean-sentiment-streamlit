import streamlit as st

# 퀴즈 데이터 (주관식 문제, 정답, 힌트)
questions = [
    {"question": "천 원짜리 지폐에 새겨진 인물은?", "answer": "퇴계 이황", "hint": "퇴계"},
    {"question": "스승을 뛰어넘는 제자를 비유하는 사자성어는?", "answer": "청출어람", "hint": "청출"},
    {"question": "한 가지 일에 지나치게 몰두하던 사람이 갑자기 극도의 신체적, 정신적 피로로 무기력증과 자기혐오에 빠지는 이 현상은?", "answer": "번아웃", "hint": "ㅂㅇㅇ"},
    {"question": "나침반에서 S극이 가리키는 방향은 동서남북 중 어디인가?", "answer": "남쪽" or "남", "hint": "아래쪽"},
    {"question": "한 해의 첫 보름이자 보름달이 뜨는 날은?", "answer": "정월대보름", "hint": "ㅈㅇㄷㅂㄹ"},
    {"question": "고기로 만드는 양념이 들어간 이탈리아 계열의 미국식 살라미. 주로 피자 토핑에 쓰이는 재료의 이름은?", "answer": "페퍼로니", "hint": "ㅍㅍㄹㄴ"},
    {"question": "대한민국 제 1대 대통령의 이름을 말하시오.", "answer": "이승만", "hint": "ㅇㅅㅁ"},
    {"question": "본래는 주식 용어이나, 일상에서 더 큰 손해를 막기 위해 작은 손해를 감수하고 어떤 행위를 그만 둠의 의미로 활용되는 단어는?", "answer": "손절", "hint": "ㅅㅈ"},
    {"question": " 이순신 장군이 육전에서 사용되던 학익진 전술을 최초로 해전에 도입했던 전투는?", "answer": "한산도대첩", "hint": "ㅎㅅㄷ대첩"},
    {"question": "우리나라에서 가장 큰 섬은 어디인가요?", "answer": "제주도", "hint": "귤"},
    # 추가 문제들 (200개 문제 추가)
]

# 앱의 제목
st.title('상식 퀴즈 앱')

# 퀴즈 시작 버튼
if st.button('퀴즈 시작'):
    st.session_state['score'] = 0  # 점수 초기화
    st.session_state['current_question'] = 0  # 첫 문제로 시작

# 현재 문제 번호 가져오기
current_question = st.session_state.get('current_question', 0)

if current_question < len(questions):
    # 문제 가져오기
    question = questions[current_question]
    
    # 문제 출력
    st.subheader(question['question'])
    
    # 주관식 입력란
    user_answer = st.text_input("답을 입력하세요")
    
    # 힌트 제공 버튼
    if st.button("힌트 제공"):
        st.info(question['hint'])  # 힌트 내용 출력
    
    # 답을 확인할 버튼
    if st.button('답 확인'):
        # 정답 비교
        if user_answer.strip().lower() == question['answer'].lower():
            st.success('정답입니다!')
            st.session_state['score'] += 1  # 점수 증가
        else:
            st.error(f'틀렸습니다! 정답은 "{question["answer"]}"입니다.')
        
        # 다음 문제로 넘어가기 버튼
        if current_question < len(questions) - 1:
            if st.button('다음 문제로'):
                st.session_state['current_question'] += 1
        else:
            st.write(f'퀴즈 종료! 총 {st.session_state["score"]}점입니다.')

else:
    st.write('퀴즈 종료! 다시 시작하려면 버튼을 클릭하세요.')
