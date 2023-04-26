import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts.prompt import PromptTemplate


class Chatbot:
    _template = """다음 대화와 후속 질문이 주어지면 후속 질문을 독립형 질문으로 바꾸십시오.
    질문이 CSV 파일의 정보에 관한 것이라고 가정할 수 있습니다.
    Chat History:
    {chat_history}
    Follow-up entry: {question}
    Standalone question:"""

    CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

    qa_template = """"csv 파일의 정보를 기반으로 질문에 답하는 AI 대화 비서입니다.
    csv 파일의 데이터와 질문이 제공되며 사용자가 필요한 정보를 찾도록 도와야 합니다. 
    알고 있는 정보에 대해서만 응답하십시오. 답을 지어내려고 하지 마세요.
    귀하의 답변은 짧고 친근하며 동일한 언어로 작성되어야 합니다.
    question: {question}
    =========
    {context}
    =======
    """

    QA_PROMPT = PromptTemplate(template=qa_template, input_variables=["question", "context"])

    def __init__(self, model_name, temperature, vectors):
        self.model_name = model_name
        self.temperature = temperature
        self.vectors = vectors

    def conversational_chat(self, query):
        """
        Starts a conversational chat with a model via Langchain
        """

        chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model_name=self.model_name, temperature=self.temperature),
            condense_question_prompt=self.CONDENSE_QUESTION_PROMPT,
            qa_prompt=self.QA_PROMPT,
            retriever=self.vectors.as_retriever(),
        )
        result = chain({"question": query, "chat_history": st.session_state["history"]})

        st.session_state["history"].append((query, result["answer"]))

        return result["answer"]