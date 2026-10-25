from langchain_core.tools import tool



@tool
#this is used to convert the python function in the tool
def calculator(a:int, b: int) -> int:
    #here it is meandatory to write the docstring so that LLM can refer to that for the task performance
    """Multiply two numbers."""
    return a*b




