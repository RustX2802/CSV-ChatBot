import streamlit as st


class Layout:
    def show_header(self):
        """
        Displays the header of the app
        """
        st.markdown(
            """
            <h1 style='text-align: center;'>CSV-ChatBot, Talk with your  csv-data ! / CSV-ChatBot, csv 데이터로 대화하세요! 💬</h1>
            """,
            unsafe_allow_html=True,
        )

    def show_api_key_missing(self):
        """
        Displays a message if the user has not entered an API key
        """
        st.markdown(
            """
            <div style='text-align: center;'>
                <h4>Enter your <a href="https://platform.openai.com/account/api-keys" target="_blank">OpenAI API key</a> to start chatting / 채팅을 시작하려면 <a href="https://platform.openai.com/account/api-keys" target="_blank">OpenAI API 키</a>를 입력하세요.  😉</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def prompt_form(self):
        """
        Displays the prompt form
        """
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query: / 질문:",
                placeholder="Ask me anything about the document... / 문서에 대해 무엇이든 물어보세요...",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="Send / 보내주세요")
            is_ready = submit_button and user_input
        return is_ready, user_input