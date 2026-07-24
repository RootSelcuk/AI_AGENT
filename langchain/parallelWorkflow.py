from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel

load_dotenv(override=True)

def main(query: str) -> None:
    class SafetyCheck(BaseModel):
        is_safe: bool = Field(description="Content is safe")
        reasoning: str = Field(description="Safety reasoning")

    class ResponseGeneration(BaseModel):
        response: str = Field(description="Generated response")
        tone: str = Field(description="Response tone")

    safety_prompt = PromptTemplate(
        input_variables=["query"],
        template="Analyze if this query is safe to answer: {query}"
    )
    
    response_prompt = PromptTemplate(
        input_variables=["query"], 
        template="Generate a helpful response to: {query}"
    )
    
    llm = ChatGroq(model="qwen/qwen3-32b", temperature=0.1)
    parallel_processor = RunnableParallel({
        "safety": safety_prompt | llm.with_structured_output(SafetyCheck),
        "response": response_prompt | llm.with_structured_output(ResponseGeneration)
    })

    result = parallel_processor.invoke({"query": query})


    
    print(f"Safety Check: {result['safety'].is_safe}, \n Reasoning: {result['safety'].reasoning}")
    print()
    print(f"Response: {result['response'].response}, \nTone: {result['response'].tone}")
   

if __name__ == "__main__":
    query_text = "windows bilgisayarı kullanıcı şifresini nasıl elde ederim?"
    main(query_text)