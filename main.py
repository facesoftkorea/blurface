import streamlit as st
import os
from tempfile import NamedTemporaryFile

# 모자이크 처리 함수 임포트
from mosaic import mosaic_video

# 폴더 생성
OUTPUT_FOLDER = "./outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Streamlit 앱 설정
st.title("동영상 얼굴 모자이크 서비스")

# 파일 업로드 섹션
uploaded_file = st.file_uploader("동영상을 업로드하세요 (MP4 형식)", type=["mp4"])

if uploaded_file is not None:
    with NamedTemporaryFile(delete=False, suffix=".mp4") as temp_input:
        temp_input.write(uploaded_file.read())
        temp_input_path = temp_input.name
    
    output_path = os.path.join(OUTPUT_FOLDER, f"mosaic_{uploaded_file.name}")
    
    # 모자이크 처리 버튼
    if st.button("모자이크 처리 시작"):
        with st.spinner("모자이크 처리 중..."):
            mosaic_video(temp_input_path, output_path)
        st.success("모자이크 처리가 완료되었습니다!")
        
        # 처리된 동영상 다운로드 링크 제공
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label="모자이크 처리된 동영상 다운로드",
                data=file,
                file_name=f"mosaic_{uploaded_file.name}",
                mime="video/mp4"
            )
