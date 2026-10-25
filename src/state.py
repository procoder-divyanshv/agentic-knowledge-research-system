# from typing import TypedDict

# class State(TypedDict):
#     question: str
#     response : str

from langgraph.graph import MessagesState


class State(MessagesState):
    pass


# this is the application of the inheritance as State class inherited the features and the schema of the MessagesState class 

