from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
import requests
import os
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage, AIMessage

# from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv(override=True)

# def run_with_no_tools(prompt: str) -> str:
#     prompt_template = PromptTemplate.from_template(
#         "Sen bir yapay zeka asistanısın. Soruyu cevapla: {question}"
#     )
#     llm = ChatGroq(model="qwen/qwen3-32b", temperature=0)
#     output_parser = StrOutputParser()

#     chain = (
#         prompt_template
#         | llm
#         | output_parser
#     )

#     response = chain.invoke({"question": prompt})

#     return response

@tool
def get_current_weather() -> dict:
    """
    Get the current weather for the user's location.
    """
    try:
        ip_url = "https://ipinfo.io/json"
        ip_response = requests.get(ip_url, timeout=10)
        ip_response.raise_for_status()
        ip_data = ip_response.json()

        latitude, longitude = ip_data["loc"].split(",")
        city = ip_data.get("city", "Bilinmiyor")
        region = ip_data.get("region", "")
        country = ip_data.get("country", "")

        weather_response = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true",
            timeout=10
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current_weather"]
        return {
            "temperature": current["temperature"],
            "unit": "celsius",
            "location": f"{city}, {region}, {country}".strip(", "),
            "latitude": latitude,
            "longitude": longitude
        }

    except requests.RequestException as e:
        return {"error": f"Hava durumu alınamadı: {str(e)}", "temperature": None, "location": None}
    except KeyError as e:
        return {"error": f"Beklenmeyen veri formatı: {str(e)}", "temperature": None, "location": None}

def run_with_tools(prompt: str) -> str:
    prompt_template = PromptTemplate.from_template(
        "Sen bir yapay zeka asistanısın. Soruyu cevapla: {question}"
    )
    llm = ChatGroq(model="qwen/qwen3-32b", temperature=0)
    llm_with_tools = llm.bind_tools([get_current_weather])

    chain = (
        prompt_template
        | llm_with_tools
    )

    response = chain.invoke({"question": prompt})

    if hasattr(response, "tool_calls"):
        tool_call = response.tool_calls[0]
        
        if tool_call['name'] == "get_current_weather":
            current_weather = get_current_weather.invoke({})

            messages = [
                HumanMessage(content=prompt),
                AIMessage(content=response.content, tool_calls=[tool_call]),
                ToolMessage(content=f"Current weather: {current_weather}", tool_call_id=tool_call['id'])
            ]

            response = llm_with_tools.invoke(messages)

    return response





prompt: str = "Şu an  hava kaç derece? Ve hangi konumdaki hava durumunu söyle"

# response_llm_with_no_tools = run_with_no_tools(prompt)
# print(response_llm_with_no_tools)

response_llm_with_tools = run_with_tools(prompt)
print(response_llm_with_tools.content)