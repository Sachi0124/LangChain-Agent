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

![Image](https://images.openai.com/static-rsc-4/5_gKJWZ8bXke77EvssYYv5_xROW-ehQ7IR5439EYtsRlwpylUz96b_InC1jwmI5EXBBiFqBwo9o6SguUjS1nKGJXaT8o4MGc8WDwv6v1ItyjMl7REHGdLbs0i4dpjVhk6cAzNKiZyjPEHSdSGV7XaJiNU9OwqjXH3lIKRAlqKFEJidYuW_QLlWbrQRypSucI?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/icDK1Qfm3v5dm1eeey-0s-ydRZcqEeFxdDirEFfVpyXSz5HZbEZ-EPUiF_M5MfFORLfOcZlHTqL4ZE1CNV3nSpUHVXZIJcRZr1JUQ2helbhfmyKN4ECdtGGmItVRbIpxxusmPTlvdiVHEAclO2Hnoa2Cxhx4_-m1usHoEFrGbNWdchAjAWihsuuUKJhO9rsq?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/yhXkmMckrWF5ku064g4hyIy-7ANpv9Awze_pb-ndJhEhxv7ZLHYs94Mj4ThFaIKURIMVZ6IO5x5Re4TfCiMPz2M_IeKDatdCFFTGJ9_n1Xce1QIb_BII3iZKg3TWoso7QWYe4GYL23rt6UKC0N4bUjrYG4oOHRjj4lPFCJx-bs_1Oxmsih7c4SdaO_Ebg2Fu?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/bK4c4jtDBSejLJZmLCNqlMHBZPObLHwjC0z5-Vl2lh4CcE_xzs2wwUipv2Oh41vrl4hePhgRzmaLj69QRpS6DJUdfAbK1NW7QDSH3-b46aWBmzWiA6nJYi76TqSappejUGzHY1yzh_rAtOI0o9U0dzphsSS_h9WJl0oCFaljYKQYZcsaZypF7pzqs66aF72n?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ZnxZo_NBH7QQgcKuHgdHg9AjISKwOELmXatJ7YGlJeXAUyAdIbIovlQUdwpJete8w6eto4hmpfIblj2TxriPdNGVxtFd90KwbgMF0aZJbiHyVV1DZDHWCqMJOiPoghMaj4c3Ps6MggLTNqBZnUrcGOEKCcRLFdMu3dUi8D5QxAdkGQfFQfOZ7YpBkVzRjzjR?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/JrjYSRvE7pFsyFfBkVjdAsut5M4GielLT30TN7_ThOcU9GR0vGMSFl75gjX0qgNK7N5ltV_hEptatPerHAoYR5Ds5oRMCA1hEx7nOA-su2dGgBFZCEEyRfJdpQ78axdYHSISU9JsWS4HJdUrlhW6yjOgjbs25FNiw_JtIjpJqGidvFh5i2tflNtaUSr_5t7B?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/gjz2PC2MaG7_yH5cU-7VpoCVE879TpFT6PQytJR5CtLFlLwa4ndFNM8pMIRdxBN1k2Q1Eg6nBe37BBhxYak23qlNvtT9te_iKA5DUqCrIjNlePDYiso4xu-BeGnZztxORbiLZVj-R3ZOgWaSHgTdkrxHcNvRG5lhrrgofCslc1If6Zz_LcnVrMjFNcy-bKc9?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/b71aN9VWuK73QmGfsJEOYyXh-PGnrD_GLCjXHv1KUkpdmDAQnKW4KB5_KN10rEGJatRFxUdRB5CCWcn2W2F_bHleI6XA0YGNOXDppqD5EQU35KMBJdQNwAVqygu7_i8cyv80SNx2oGCub7PU00vReeq7mO1a5okSctk0MuAjNDFtcwpavXIlHcSbmsGB7Xh0?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/V5RZZ__OhS3pMDqjN3H6A5LIi261Y8U6OIU8yW-g88bDfx7N1IgkiWSMDWtjBMPy17iju5cO9P-faqzSg8pYPl6ki76R7SOOBlQIHpLx3JfbEMrDBPyhijSyw-hWSvn_KwBoe8-BXlfUclacOvLz7eghuKgbWvuOhR6-nz8nwzvr9DHtLO5bpgHymgLgn2go?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/AxpxOPUjjc4Ut6W8WN2EI9R3JEJfhqC_D5UaBYL5D0gjhKm-dq4v6tsZVR34OXRy0x4vUkACSVWDtnFi1hsNmMhpzzCobIcr45tj54en5Rgu6DwlqTq9K4TZiJs3g3xIzKNtnPHRzAX0NmTFwcjALUUwIdWXPDHaQ1NsXNqJC0Y7xa5bdpU7E_1QDwyvEKq0?purpose=fullsize)

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

# 🖥 Sample UI

### Weather Query Response

![Image](https://images.openai.com/static-rsc-4/jNczVsw4diR8y9G3tGgKPjlmGtlVlMzYhZnnsnh5oWB2fsf56DazNzT_fAD-u044xD4iLoItdpcdOaeP2z3Zu3trk14TfQU8PkjMgfHseS7dcJ8jiiXzsehBi1ir_abycT7IAftHi2GoBCa3bkUpCwRKMDOIaz_EjE2Mre3k-kNXJqGFaQnE197C-sTWyXdi?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/pF3HauLyfLbDkHJ0oFLXd6ZR0Iz632joLU1rmbv1-zRAyM34TDs_qiAyjjMIomiV1BLoPM5BzWxaDp2s4309leY7W7NrNW2gxtnrNFqn4Xc_j1gNrxIA_y5vL8I6m0JlyEHlCTHhKG4EolqzFkZ8alDTk_1sWFv2ACcZxRpBXBW1P9DFAESoMVii_nMHLwLa?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/lsFCwHoBwL_a1mKGtuH81nrKrNKT2knBenhrfaT7nlKuPoF6tepyUS-uURN27BzoxUkkkY7rcBp33Zz7LfCNds0jWi3S4IWYuMdRkfFGZa3ujHEjHFMPH6uariKa_dWP9XccvcBHm3v0U90h3pp-zpJa9lWCeZG9G1aF5PaR8AIGjlJM9Co_MjK3hG_sIpPK?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/qdzLSy6miYnjzN1Na-3dRLW7AwtGUEGzxZugA9oDo_SZOs9Ju_grBNplaDmfsKc_pu7D_klz_UA5dxXTkgdNYcHEfFG48IlpPX6vQjnQ4Zo3_FMjTLWj8QP_NfJAiCjB7ws47xozqmeFSh1F5DZZU99CxPS_pYwskXBDaRCdxIkYy9XaT2iUbGMM2ZG9rSVN?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Z3SCvDfrjuFZzcsxoGQ1SZeQ8iZfRDAOzNzs7K6E7N8oA3lTepjUiVWGfv7iEMhh6Jja5yuoc6UoNYdxrwG7Utkr6V_mX_eOSPfIxY82JVqR1TGLh_8VdWvNekrrE2GSGIbsJ1lOrkJ9EBCCRVhiqp7ZYZtzbWOr1Hjs1fNdZNzZDRLFp-w6uXfgccuB5zrO?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/jk-bG6dX_XQ0WOZqMxpiYmr-0tG4rzQAaNF9iMzI25T04tV-CNVE7RLPUpub9Lw9qoDjrNMKSSLGwVc6XPE90IjgEWCpaU3DzVGs4X2ononH-ZncFQgn6DXzB7YGL6rwW1g7GdZXtNdzfDOZWAZn82Vmm3ioZplZRU0rr1RdfZaLpz1wNmVA3z9txbQQ5GZq?purpose=fullsize)

### General Knowledge Query

![Image](https://images.openai.com/static-rsc-4/JKSP_Ov-WjZumnnVN1yTyu_cKXs4fVFgFJ35G-qJmFfW6A8epuYBxNnH2rTvPGJMsKDU-7jgYfRLRUnIzuFzSMrBIltjJsECGfgO02KSJR7dvBgP5R1-07Mp6iR5KfsPQHu5gugb2DKOiL5SOcEJhOmhlySRf2IC_uDDGI-Dj6SAik41vzUTybFyPxqXjU-9?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/9ngi5PNDCcA0Hd4ws3bOCxgbld55v-HOndWp8vTEPBZulQmpa3cgeYVMFUi25uFMgewJjq4wfxW6X5mPn-6mli8i8Z8MECPjufUxOr96zXy8d6_pfSj31oY4DgBne52Vfz1tNiphdOWVC3UvWevdYk4r-jC-FYkErc2JZQEzrXw3g76rkUwZ6y4UtfhpSGyU?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/tEi0OO7axNwAOF9z5LAG5QiGR9DYME_rodxVnX7hgB7auNjhQArMT-vO3oHIA7gP4rbaQW6e1m5aAl80XrIYyhC_0axnXXxVowI-mJ1nEw1B20vPtE6Tv87nT_lltRdUzb289BFnyUS1vXUP3DZ0-6rZLxurkw6jwGr8odHkvamvb_WSUROKY6Fl0Dy1sB3L?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Da341EMVbDDqcxRhUPqLEMbG90NFXoCJ4Pkc459rcFgFjmN6ZE5GtY_T0f477vebE_EU1Y-Uc65LMBNuXGYBNwpFSIgBRMIVjupu-LKY9O5-QxBW2egO1VKAoGz-0jAioCpACkxHbrdLhiLUkuRfyozPX0EqhXaHZQ80M2IZNdlBvL-qZ577UHOq2peF8Uik?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/iNOtTu1DazQBJKUyKXIoaXYdOmfCunNiBdxQrY2FFNYcWzBK9xkAcYkj1Q4rnGcO6BIR6l0uSmSejEcJgRLSacFYDnEsoPL4-H0Ko_zK1HyhPfZwnJ7LwWRdq8pYF3i5Hhbp5c1OATbq6VmxTdUF_rVvmYSOnKBDNCd29dbX4cHQ2UAvdgaPm-lzNkhOxSRA?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/xdF1IVdlFUnD7IrjR_YWQNcJ2crKRH0d5DSMkHeYG1OvCWiqwh_wc6ZgeLw8wD3sykVIhaccjnZo--jDIwJKt4mhvObow2m1WHZa8jnh65JRbo0OaOHGmx29Zjlhue2OV9aQrzGcDNTeHHz3i15runTTvLQgag7UIQjsVl5ne5q3xKvn3fE5hibhmdWuJSPF?purpose=fullsize)

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