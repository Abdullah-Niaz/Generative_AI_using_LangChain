from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    # give me the repo/model id
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # task you want to perform from this model
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the cpital of pakistan")
print(result.content)