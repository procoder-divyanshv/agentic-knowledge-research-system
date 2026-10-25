import os
import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.state import State
from src.tools import calculator




load_dotenv()


# we have to declare the model outside any node so that it will be universal model for the whole workflow and need not to be recreated.
llm = ChatGoogleGenerativeAI(model = "gemini-3.8-flash", temperature=0.7)
llm = llm.bind_tools([calculator]) #binded the tool created 
#now write the node that calls the llm and return the response 

def llm_node(state: State):
    start_time = time.perf_counter()
    response = llm.invoke(state["messages"])
    end_time = time.perf_counter()
    print(f"LLM call time: {end_time - start_time:.2f} seconds")
    # state["response"]= response.content
    return {
        "messages" : [response]

    }



