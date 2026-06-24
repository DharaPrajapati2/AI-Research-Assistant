from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = PydanticOutputParser(
    pydantic_object=ResearchResponse
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that helps generate research papers.

            Answer the user's query and return the response in the exact format below.

            {format_instructions}
            """
        ),
        ("human", "{query}")
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)

chain = prompt | llm | parser

query = input("What can I help you research? ")

response = chain.invoke(
    {
        "query": query
    }
)

print("\nResearch Result:\n")
print(response)