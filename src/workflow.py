from langgraph.graph import StateGraph, START, END

from langgraph.prebuilt import ToolNode, tools_condition
from src.state import State
from src.nodes import llm_node
from src.tools import calculator




graph_builder = StateGraph(State)

#nodes
graph_builder.add_node("llm", llm_node)
graph_builder.add_node("tools", ToolNode([calculator]))


graph_builder.add_edge(START, "llm")
graph_builder.add_conditional_edges("llm", tools_condition)
graph_builder.add_edge("tools", "llm")  #this will actually create the loop of LLM->tools->LLM




workflow = graph_builder.compile()
# now wrokflow contians the executable graph but we have to invoke it from the main.py file 
