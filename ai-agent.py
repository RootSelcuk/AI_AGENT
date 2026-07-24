import streamlit as st
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv
load_dotenv(override=True)


modelgpt = init_chat_model("openai/gpt-oss-120b", model_provider="groq")

@st.cache_resource
def agent_olustur():
    return create_agent(model=modelgpt,
    tools=[]
    )

agent=agent_olustur()
st.set_page_config(page_title="basit agent AI",page_icon="🤖")
st.title("Simple Agent AI")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for mesaj in st.session_state.messages:
    with st.chat_message(mesaj["role"]):
        st.markdown(mesaj["content"])

if prompt:= st.chat_input("SORU NEDİR?"):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Düşünüyorum"):
            response = agent.invoke({"messages":st.session_state.messages })
        output=response["messages"][-1].content
        st.markdown(output)
    st.session_state.messages.append({"role":"assistant","content":output})