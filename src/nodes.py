import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.state import State




load_dotenv()


# we have to declare the model outside any node so that it will be universal model for the whole workflow and need not to be recreated.
llm = ChatGoogleGenerativeAI(model = "gemini-3.8-flash", temperature=0.7)

#now write the node that calls the llm and return the response 

def llm_node(state: State):
    response = llm.invoke(state["question"])
    # state["response"]= response.content
    return {
        "response" : response.content

    }



