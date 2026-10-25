from langchain_core.tools import tool
from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()
# abb tavily client bnayenge

client = TavilyClient() #this is the client used to send the request to the tavily 

@tool
#this is used to convert the python function in the tool
def calculator(a:int, b: int) -> int:
    #here it is meandatory to write the docstring so that LLM can refer to that for the task performance
    """Multiply two numbers."""
    return a*b


@tool
def search_web(query: str)->str:
    """Search the web for current or external information.""" #this is the doctring of this tool 
    response =  client.search(
        query= query,
        search_depth= "advanced",
        max_results = 2,

    )
    results = response.get("results", [])
    if not results:
        return "No result found."

    formatted_results = []

    for result in results:
        title = result.get("title", "No title")
        url = result.get("url", "No url")
        content = result.get("content", "No content")


        formatted_results.append(
            f"Title: {title}\n"
            f"URL: {url}\n"
            f"Content: {content}\n"

        )
    
    return "\n------\n".join(formatted_results)


TOOLS = [calculator, search_web]
