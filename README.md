# LangChain Chat Agent 🚀

A clean and lightweight AI-powered chat assistant built using [LangChain](https://www.langchain.com/?utm_source=chatgpt.com), [Streamlit](https://streamlit.io/?utm_source=chatgpt.com), and [Google Gemini API](https://ai.google.dev/?utm_source=chatgpt.com).

This project combines:

* Conversational AI
* Web Search
* Weather Search
* News Fetching
* YouTube Search
* Smart Response Generation
* Streamlit Chat UI

The agent intelligently decides when to search the web and when to directly answer using the LLM.

---

## 📸 Project Preview

### Main Chat UI
## 📸 Project Preview

### Main Chat UI

<img width="100%" src="images/Screenshot 2026-05-09 233304.png">

<img width="100%" src="images/Screenshot 2026-05-09 233713.png">

<img width="100%" src="images/Screenshot 2026-05-09 233815.png">
---

# ✨ Features

* 🤖 AI Chat Agent using Gemini 2.5 Flash
* 🌐 DuckDuckGo Web Search Integration
* 🎥 YouTube Video Search
* 🌦 Real-Time Weather Information
* 📰 Latest News Fetching
* ⚡ Fast Responses with Query Caching
* 🧠 Smart Query Handling
* 💬 Modern Chat UI with Streamlit
* 🔄 Rate Limiting for Stable API Usage
* 📺 Embedded YouTube Video Playback
* 🛡 Error Handling & Fallback Responses

---

# 🛠 Tech Stack

### Backend

* Python
* LangChain
* Gemini API
* DuckDuckGo Search
* News API
* OpenWeather API

### Frontend

* Streamlit

### APIs Used

* Google Gemini API
* OpenWeather API
* News API

---

# 📂 Project Structure

```bash
project/
│
├── agent.py          # Main AI agent logic
├── tools.py          # External tools and integrations
├── ui.py             # Streamlit frontend UI
├── .gitignore
└── README.md
```

---

# ⚙️ How It Works

## 1. User asks a question

Example:

```text
What is Bengaluru weather?
```

---

## 2. Agent analyzes the query

The system checks:

* Is it a simple greeting?
* Does it require search?
* Does it require weather/news/video tools?

---

## 3. Tool Execution

Depending on the query:

* Weather → OpenWeather API
* News → News API
* Videos → YouTube Search
* General Information → DuckDuckGo Search

---

## 4. Gemini Generates Final Response

The search result is passed into Gemini for generating a natural response.

---

# 🧠 Agent Architecture

```text
User Input
     ↓
Streamlit UI
     ↓
LangChain Agent
     ↓
Tool Selection
 ┌───────────────┐
 │ Web Search    │
 │ Weather API   │
 │ News API      │
 │ YouTube Tool  │
 └───────────────┘
     ↓
Gemini LLM
     ↓
Final Response
```

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/langchain-chat-agent.git
cd langchain-chat-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Keys Setup

Inside `agent.py`, add your API keys:

```python
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY"
OPENWEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
```

---

# ▶️ Run Project

```bash
streamlit run ui.py
```

Then open:

```text
http://localhost:8501
```

---

# 💡 Example Queries

```text
What is Bengaluru weather?

Latest AI news

Search YouTube videos about LangChain

Who is Elon Musk?

Explain quantum computing
```

---

# 📜 Core Files Explanation

## `agent.py`

Main brain of the chatbot:

* Initializes Gemini model
* Manages tools
* Handles caching
* Controls rate limiting
* Generates responses



---

## `tools.py`

Contains all external integrations:

* DuckDuckGo Search
* YouTube Search
* Weather API
* News API



---

## `ui.py`

Frontend built using Streamlit:

* Chat interface
* Message history
* Spinner loading
* YouTube video embedding



---

# 🚀 Optimization Features

## Query Caching

Repeated queries are cached for:

* Faster responses
* Reduced API calls

---

## Rate Limiting

The project prevents excessive searches by:

* Adding delays between requests
* Avoiding API overload

---

## Fallback Handling

If search fails:

* Gemini still generates a response

---

# 🎯 Future Improvements

* Voice Assistant Integration
* Memory-based Conversations
* PDF Question Answering
* RAG Pipeline
* Database Chat History
* Authentication System
* Multi-Agent Workflow
* LangGraph Integration
* Dark/Light Theme Toggle

---

# 📈 Why This Project is Good

This project demonstrates:

* AI Integration
* Tool Calling
* API Handling
* LangChain Concepts
* LLM Application Development
* Streamlit Deployment
* Real-Time Information Retrieval

# 🤝 Contributing

Contributions are welcome.

```bash
Fork the repository
Create your feature branch
Commit your changes
Push to the branch
Create a Pull Request
```

---

# 👨‍💻 Author

Sachith.c

Information Science Engineering Student
