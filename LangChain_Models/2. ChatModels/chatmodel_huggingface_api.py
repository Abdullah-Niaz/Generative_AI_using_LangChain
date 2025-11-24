from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# # above model does not support the chat application api 
# # model = ChatHuggingFace(llm = llm)
# # result = model.invoke("what is the capital of pakistan")
# # print(result.content)


print(os.getenv("HUGGINGFACEHUB_API_TOKEN")) 

llm = HuggingFaceEndpoint(
    repo_id="tiiuae/falcon-7b-instruct",
    task="text-generation"
)

result = llm.invoke("what is the capital of Pakistan")
print(result)
