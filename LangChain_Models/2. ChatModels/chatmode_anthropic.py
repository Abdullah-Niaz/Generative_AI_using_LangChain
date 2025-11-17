from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()


model = ChatAnthropic(model="claude-3.-5-sonnet-00000000")

result = model.invoke("what is the cpital of pakistan")

print(result.content)
