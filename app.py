import streamlit as st

page_1 = st.Page("page_1.py", title = "홈")
page_2 = st.Page("page_2.py", title = "챗봇")
page_3 = st.Page("page_3.py", title = "로그인")

pages = st.navigation([page_1, page_2, page_3], position = "top")

pages.run()
# st.title("우리 회사 챗봇")

# st.write("채팅을 입력하세요.")

# st.markdown("안녕하세요 *부트캠프 참여자* 여러분!")

# st.badge("성공!", icon=":material/check:", color="green")

# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language="python")