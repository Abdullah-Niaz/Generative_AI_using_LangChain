## Components of LangChain?
    1. Models
    2. Prompts
    3. Chains
    4. Memory
    5. Indexes
    6. Agents



### **1. Models**
The **brain** of your app — the LLM (Large Language Model) that generates or interprets text.

**Examples:** OpenAI GPT, Claude, Gemini, LLaMA, etc.

**Use case example:**

```python
from langchain.llms import OpenAI
llm = OpenAI(model_name="gpt-3.5-turbo")
response = llm("What is LangChain?")
```

**Think of it as:** the “engine” that powers all reasoning and text generation.

---

### **2. Prompts**
A **template** that structures how you talk to the model.

You can insert variables dynamically — so your instructions are clean, reusable, and clear.

Other Prompts Types:
    . Role Based Prompts
    . Few shots Prompts

**Example:**

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in one paragraph."
)
```

**Think of it as:** the **question format** or the “input design” that controls how the model behaves.

---

### **3. Chains**
A **sequence of steps** connecting inputs → model → output.

You can join multiple operations like:

* Prompt the model
* process response
* send it to another model

**Example:**

```python
from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("Machine Learning"))
```

**Think of it as:** a **pipeline** — how tasks flow from start to finish.

---

## **4. Indexes**
A structure that helps **store and search large text data** efficiently using **embeddings** (numerical representations of meaning).

You typically store documents in **vector databases** (like Chroma, FAISS, or Pinecone).

**Example:**

```python 
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
db = Chroma.from_texts(["LangChain connects LLMs with data."], embeddings)
```

**Think of it as:** your **knowledge base** — where your app looks up information when asked a question.

---

## **5. Memory**
Allows your system to **remember context** — e.g., what was said before in the conversation.

**Without memory:** Every prompt is treated independently.
**With memory:** It keeps continuity.

**Example:**

```python
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
memory.save_context({"user": "Hi"}, {"bot": "Hello!"})
```

**Think of it as:** your AI’s **short-term or long-term memory**.

---

## **6. Agents**
Agents can **decide** what actions to take — like calling APIs, using tools, or retrieving data — based on the user query.

They bring reasoning + decision-making to your app.

**Example:**

```python
from langchain.agents import initialize_agent, load_tools

tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")
agent.run("What’s 25% of the population of Pakistan?")
```

**Think of it as:** your app’s **“smart assistant”** — it plans steps and executes them intelligently.

---

## How They Work Together

Here’s the **flow**:

```
User Input
   ↓
Prompt Template  → formats question
   ↓
Model (LLM)  → generates response
   ↓
Chain  → connects logic and steps
   ↓
Index  → fetches data if needed
   ↓
Memory  → recalls past info
   ↓
Agent  → decides actions or tool usage
```