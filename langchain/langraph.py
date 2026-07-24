from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage

load_dotenv(override=True)

class AgentState(TypedDict):
    messages: list

# define Node
def chat_node(state: AgentState) -> AgentState:
    llm = ChatGroq(model="qwen/qwen3-32b")

    messages: list = state["messages"]
    chat_response = llm.invoke(messages)

    state["messages"].append(chat_response)
    return state

graph_builder = StateGraph(AgentState)

# add nodes to grap
graph_builder.add_node("chat_node", chat_node)

# add edges to graph
graph_builder.add_edge(START, "chat_node")
graph_builder.add_edge("chat_node", END)

# build the graph
graph = graph_builder.compile()

# # # get grap image
# graph_image: bytes = graph.get_graph().draw_mermaid_png() 

# # # save the graph image
# with open("graph.png", "wb") as f:
#     f.write(graph_image)

initial_state = AgentState(messages=[])
initial_state["messages"].append(HumanMessage(content="what was the last your response?"))

response = graph.invoke(input=initial_state)
print(response)