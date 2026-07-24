from dotenv import load_dotenv
load_dotenv(override=True)
from langchain.tools import tool
@tool
def square_root(n:float) -> float:
    """ calculate the square root of a number """
    return n**0.5

from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model



modelgpt = init_chat_model('openai/gpt-oss-120b', model_provider='groq')
agent = create_react_agent(model=modelgpt, tools=[square_root])
print('Success!')