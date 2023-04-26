import streamlit as st


class Sidebar:
    MODEL_OPTIONS = ["gpt-3.5-turbo", "gpt-4"]
    TEMPERATURE_MIN_VALUE = 0.0
    TEMPERATURE_MAX_VALUE = 1.0
    TEMPERATURE_DEFAULT_VALUE = 0.0
    TEMPERATURE_STEP = 0.01

    @staticmethod
    def about():
        about = st.sidebar.expander("🤖에 대한")
        sections = [
            "#### CSV-ChatBot는 사용자가 보다 직관적인 방식으로 CSV 데이터를 논의할 수 있도록 설계된 대화형 메모리 기능을 갖춘 AI 챗봇입니다. 📄",
            "#### 그는 대규모 언어 모델을 사용하여 CSV 데이터를 더 잘 이해할 수 있도록 원활하고 상황에 맞는 자연어 상호 작용을 사용자에게 제공합니다. 🌐",
            "#### [Langchain](https://github.com/hwchase17/langchain), [OpenAI](https://platform.openai.com/docs/models/gpt-3-5) 및 [Streamlit](https://github.com/streamlit/streamlit)에 의해 구동됩니다 ⚡",
            "#### Source code : [RustX/ChatBot-CSV](https://github.com/RustX2802/CSV-ChatBot)",
        ]
        for section in sections:
            about.write(section)

    @staticmethod
    def reset_chat_button():
        if st.button("Reset chat / 채팅 재설정"):
            st.session_state["reset_chat"] = True
        st.session_state.setdefault("reset_chat", False)

    def model_selector(self):
        model = st.selectbox(label="Model / 모델", options=self.MODEL_OPTIONS)
        st.session_state["model"] = model

    def temperature_slider(self):
        temperature = st.slider(
            label="Temperature / 온도",
            min_value=self.TEMPERATURE_MIN_VALUE,
            max_value=self.TEMPERATURE_MAX_VALUE,
            value=self.TEMPERATURE_DEFAULT_VALUE,
            step=self.TEMPERATURE_STEP,
        )
        st.session_state["temperature"] = temperature
    
    def csv_agent_button(self):
        st.session_state.setdefault("show_csv_agent", False)
        if st.sidebar.button("CSV Agent"):
            st.session_state["show_csv_agent"] = not st.session_state["show_csv_agent"]

    def show_options(self):
        with st.sidebar.expander("🛠️ Tools / 도구", expanded=False):
            self.reset_chat_button()
            self.csv_agent_button()
            self.model_selector()
            self.temperature_slider()
            st.session_state.setdefault("model", self.MODEL_OPTIONS[0])
            st.session_state.setdefault("temperature", self.TEMPERATURE_DEFAULT_VALUE)