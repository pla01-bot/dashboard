import streamlit as str
import streamlit.components.v1 as components

# 페이지 레이아웃을 넓게 설정
st.set_page_config(layout="wide")

# HTML 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# 스트림릿 컴포넌트를 통해 HTML 렌더링 (가로/세로 크기 조절 가능)
components.html(html_code, height=800, scrolling=True)