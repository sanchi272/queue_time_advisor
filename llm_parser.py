from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


# Load environment variables from .env
load_dotenv()


# Structure of information extracted by the LLM
class QueueDetails(BaseModel):
    queue_length: int = Field(
        description="Approximate number of people waiting in the queue"
    )

    service_time: float = Field(
        description="Approximate service time per person in minutes"
    )

    counters: int = Field(
        description="Number of active service counters"
    )


# Create the Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0
)


# Make the LLM return structured information
structured_llm = llm.with_structured_output(QueueDetails)


# Prompt for natural-language understanding
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a queue information extraction assistant.

        Read the user's natural-language description of a queue
        and extract these three values:

        1. Number of people waiting
        2. Average service time per person in minutes
        3. Number of active counters

        If the user gives approximate values, use the closest
        reasonable numeric value.

        Return only the required structured information.
        """
    ),
    (
        "human",
        "{user_input}"
    )
])


# LangChain pipeline
queue_parser_chain = prompt | structured_llm


def parse_queue_input(user_input: str) -> dict:
    """
    Convert natural-language queue information into
    structured numerical values using LangChain + Gemini.
    """

    result = queue_parser_chain.invoke({
        "user_input": user_input
    })

    return result.model_dump()


# Simple test when this file is run directly
if __name__ == "__main__":

    sample_input = (
        "There are around 20 people waiting, "
        "2 counters are open and each person takes about 4 minutes."
    )

    result = parse_queue_input(sample_input)

    print("Extracted Queue Information:")
    print(result)