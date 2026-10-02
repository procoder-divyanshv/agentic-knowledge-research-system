from langgraph.graph import StateGraph, START, END
from src.state import State
from src.nodes import llm_node



graph_builder = StateGraph(State)

graph_builder.add_node("llm", llm_node)
graph_builder.add_edge(START, "llm")
graph_builder.add_edge("llm", END)


workflow = graph_builder.compile()
# now wrokflow contians the executable graph but we have to invoke it from the main.py file 
