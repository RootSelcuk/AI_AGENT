from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)

def main():
    
    prompt_template = PromptTemplate(
        input_variables=["name"],
        template="bana  {name}, hakkında bilgi ver?",
    )

    llm_openai = ChatGroq(
        model_name="llama-3.3-70b-versatile",
    )
    chain = prompt_template | llm_openai
    response = chain.invoke({"name": "Galatasaray"})
    print(response.content)

if __name__ == "__main__":
    main()