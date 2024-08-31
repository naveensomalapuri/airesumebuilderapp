from langchain_community.chat_models.openai import ChatOpenAI
import os
from dotenv import load_dotenv


def openmodle(prompt):
    # Load the environment variables from the .env file
    load_dotenv()


    # Retrieve the API key from the environment
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the OpenAI chat model with your API key
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

    # Get the BSON-like output from the model
    bson_output = llm.invoke(prompt)

    # Display the output
    print(bson_output)
    return bson_output