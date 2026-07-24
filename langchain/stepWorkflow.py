from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)


def main(review_text: str) -> None:
    class ReviewSentiment(BaseModel):
        sentiment: str = Field(
            description="The sentiment of the review, either 'positive', 'negative', or 'neutral'."
    ) 

    prompt_template = PromptTemplate(
        input_variables=["review"],
        template="""
        Analyze the sentiment of this product review:
        Classify it as 'positive', 'negative', or 'neutral'.

        Review Text:
        {review}
        """
    
    )

    llm_ollama = ChatGroq(model="qwen/qwen3-32b", temperature=0.7).with_structured_output(ReviewSentiment)
    chain = prompt_template | llm_ollama 
    response: ReviewSentiment = chain.invoke({"review": review_text})

    print(f"Single Step LLM Workflow Response: {response.sentiment}")

if __name__ == "__main__":
    review_text = "Tavsiye etmiyorum berbat bir ürün"
    main(review_text=review_text)