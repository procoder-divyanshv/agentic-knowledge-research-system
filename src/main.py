from src.workflow import workflow

result = workflow.invoke(
    {"question" : "What is an AI Agent? Explain in one sentence.",
     "response" : ""
     }

)

print(f"Question is : {result['question']} \n Response is : {result['response']}")


