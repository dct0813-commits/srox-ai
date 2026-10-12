import streamlit as st
from openai import OpenAI

st.title("SROX AI - 독립 모드")
api_key = st.sidebar.text_input("API Key를 입력하세요", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "너는 SROX AI다. 창조자의 독립된 AI이다."}]

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("창조자님, 무엇을 도와드릴까요?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages)
        answer = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)
