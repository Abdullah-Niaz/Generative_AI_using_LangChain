from dotenv import load_dotenv
import os

load_dotenv()
print("Loaded key:", os.getenv("HUGGINGFACEHUB_API_KEY"))
