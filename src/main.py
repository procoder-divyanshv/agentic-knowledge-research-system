import time

from src.workflow import workflow


question = "What are the latest developments in generative AI?"

start_time = time.perf_counter()

result = workflow.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
)

end_time = time.perf_counter()

final_message = result["messages"][-1]

if isinstance(final_message.content, list):
    answer = "".join(
        block["text"]
        for block in final_message.content
        if isinstance(block, dict) and block.get("type") == "text"
    )
else:
    answer = final_message.content

print(f"Question: {question}")
print(f"Answer: {answer}")
print(f"Response time: {end_time - start_time:.2f} seconds")