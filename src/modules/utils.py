import os
import pandas as pd
import streamlit as st

from modules.chatbot import Chatbot
from modules.embedder import Embedder


class Utilities:
    @staticmethod
    def load_api_key():
        """
        Loads the OpenAI API key from the .env file or from the user's input
        and returns it
        """
        if os.path.exists(".env") and os.environ.get("OPENAI_API_KEY") is not None:
            user_api_key = os.environ["OPENAI_API_KEY"]
            st.sidebar.success("API key loaded from .env / .env에서 로드된 API 키", icon="🚀")
        else:
            user_api_key = st.sidebar.text_input(
                label="#### Your OpenAI API key / OpenAI API 키 👇", placeholder="Paste your openAI API key, sk-", type="password"
            )
            if user_api_key:
                st.sidebar.success("API key loaded / API 키가 로드되었습니다", icon="🚀")
        return user_api_key

    @staticmethod
    def handle_upload():
        """
        Handles the file upload and displays the uploaded file
        """
        uploaded_file = st.sidebar.file_uploader("upload", type="csv", label_visibility="collapsed")
        if uploaded_file is not None:

            def show_user_file(uploaded_file):
                file_container = st.expander("Your CSV file : / CSV 파일:")
                shows = pd.read_csv(uploaded_file)
                uploaded_file.seek(0)
                file_container.write(shows)

            show_user_file(uploaded_file)
        else:
            st.sidebar.info(
                "👆 Upload your CSV file to get started, / 시작하려면 CSV 파일을 업로드하세요 "
                "sample for try : / 시도해 볼 샘플: [example.csv](https://drive.google.com/file/d/1g7x0Ydg5kr51Ha2XIYBSQBVUw1yYlgmc/view?usp=share_link)"
            )
            st.session_state["reset_chat"] = True
        return uploaded_file

    @staticmethod
    def setup_chatbot(uploaded_file, model, temperature):
        """
        Sets up the chatbot with the uploaded file, model, and temperature
        """
        embeds = Embedder()
        with st.spinner("Processing... / 처리 중..."):
            uploaded_file.seek(0)
            file = uploaded_file.read()
            vectors = embeds.getDocEmbeds(file, uploaded_file.name)
            chatbot = Chatbot(model, temperature, vectors)
        st.session_state["ready"] = True
        return chatbot