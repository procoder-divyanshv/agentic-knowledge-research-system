import os
import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from src.state import State
from src.tools import TOOLS




load_dotenv()


# we have to declare the model outside any node so that it will be universal model for the whole workflow and need not to be recreated.
llm = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
)
llm = llm.bind_tools(TOOLS) 
#binded the tools created 
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



