import streamlit as st
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq


from dotenv import load_dotenv
load_dotenv(override=True)



modelgroq = ChatGroq(model="openai/gpt-oss-120b")


agent = create_react_agent(model=modelgroq, tools=[])

input= st.text_input("SORU NEDİR?")
if input:
    response=agent.invoke(
     {"messages":[{"role":"user","content":input}]}
        )   
    st.write(response["messages"][-1].content)