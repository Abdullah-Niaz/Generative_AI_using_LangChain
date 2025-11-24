from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFacePipeline(
#     model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = "text-generation",
#     max_new_tokens = 100
# )
from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)

# result = model.invoke("What is the capital of pakistan")
# print(result.content)