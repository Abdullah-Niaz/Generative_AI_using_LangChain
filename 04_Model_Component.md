## Models
The Model Component in LangChain is a crucial part of framework, designed to facilitate interactions with various language models and embedding models.

It abstracts the complexity of working directly with different LLMs, chat models and embedding models, providign a uniform interface to communicate with them. This makes it easier to build applications taht rely on AI-Generated text, text embeddings for similarity search, and retrieval augmented generation(RAG).


### Types of Models:
    1. Language Models
        i. LLMs
        ii. Chat Models 
    2. Embedding MOdels

### 1. LLMs
These are general-purpose models used for raw text generation.
They take plain text as input and return plain text as output.

Traditionally, these models were the foundation of NLP systems, but modern applications now often prefer chat-based models for interactive and structured outputs.

### 2. Chat Models
Chat Models are language models specialized for conversational tasks.
They take a sequence of messages as input and return chat messages as output — unlike LLMs, which handle plain text.

These are newer models and are more widely used today compared to traditional LLMs.

### Language Models 
    i. Closed source
        a. OpenAI
        b. Cloude
        c. Gemmnai
    ii. Open source
        a. Hugging face




### Embedding Models
    i. Closed Source
    ii. Open Source