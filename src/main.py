from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message: str


def hello_node(state: State):
    return {
        "message" : f"Hello you said, {state['message']}"
    }


graph_builder = StateGraph(State)

graph_builder.add_node("hello", hello_node)
graph_builder.add_edge(START, "hello")
graph_builder.add_edge("hello", END)

graph = graph_builder.compile()

result = graph.invoke({"message": "i want to create the AI-Agent"})
print(result)


