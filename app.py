import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


def init():
    load_dotenv()
    if os.getenv('OPENAI_API_KEY') is None or os.getenv('OPENAI_API_KEY') == '':
        print("Set the OPENAI_API_KEY environment variable")

    st.set_page_config(
        page_title="ChatBot",
        page_icon="🤖"
    )


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant. Your Name is Manick Baasha")
        ]

    st.header("ChatGPT: Baasha Version")

    with st.sidebar:
        user_input = st.text_input("Enter your question:", key="user_input")

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))

        with st.spinner(text="Processing..."):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    messages = st.session_state.get("messages", [])
    for i, prompt in enumerate(messages):
        if i >= 1:
            if i % 2 == 0:
                message(prompt.content, is_user=False, key=f'{i}_ai')
            else:
                message(prompt.content, is_user=True, key=f'{i}_user')


if __name__ == "__main__":
    main()
