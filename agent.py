# agent.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import Tool
from tools import (
    multi_web_search,
    youtube_search,
    weather_search,
    news_search,
)
import time

# -----------------------
#  Rate Limiting
# -----------------------
last_search_time = 0
min_search_interval = 2  # Minimum 2 seconds between searches
search_cache = {}

# -----------------------
#  API Keys
# -----------------------
GOOGLE_API_KEY =  "your_api_key_here"  # free
OPENWEATHER_API_KEY = "your_api_key_here"  # free
NEWS_API_KEY = "your_api_key_here"  # free

# -----------------------
# Setup LLM
# -----------------------
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7,
    )

    # -----------------------
    # Wrap Tools  
    # -----------------------
    tools = [
        Tool(
            name="MultiWebSearch",
            func=multi_web_search,
            description="Search DuckDuckGo, Wikipedia, and Arxiv together for information.",
        ),
        Tool(
            name="YouTubeSearch",
            func=youtube_search,
            description="Search YouTube for videos on a given topic.",
        ),
        Tool(
            name="WeatherSearch",
            func=lambda q: weather_search(q, OPENWEATHER_API_KEY),
            description="Get current weather information for a city/location.",
        ),
        Tool(
            name="NewsSearch",
            func=lambda q: news_search(q, NEWS_API_KEY),
            description="Fetch latest news for a given topic.",
        ),
    ]

    # Simple agent that uses the LLM to decide which tool to use
    agent = llm
    agent_available = True
except Exception as e:
    print(f"Warning: Agent initialization failed: {e}")
    agent = None
    agent_available = False

# -----------------------
# Function for UI
# -----------------------
def get_agent_response(query: str) -> str:
    """Takes a user query and returns the agent's response."""
    global last_search_time
    
    if not agent_available or agent is None:
        return "Error: Agent not initialized. Check your API keys and internet connection."
    
    try:
        # Check if query is simple (greeting, small talk) - respond instantly with LLM
        simple_queries = ['hi', 'hello', 'hey', 'thanks', 'thank you', 'ok', 'okay', 'yes', 'no', 'help', 'bye', 'goodbye']
        query_lower = query.strip().lower()
        
        if any(query_lower.startswith(sq) for sq in simple_queries):
            # Simple query - respond directly with LLM without searching
            response = agent.invoke(f"Brief response: {query}")
            return response.content if hasattr(response, 'content') else str(response)
        
        # Check cache first
        if query in search_cache:
            cached_result, cache_time = search_cache[query]
            if time.time() - cache_time < 3600:  # Cache for 1 hour
                search_result = cached_result
            else:
                search_result = None
        else:
            search_result = None
        
        # For complex queries, try web search with rate limiting
        if search_result is None:
            # Rate limiting - wait if needed
            elapsed = time.time() - last_search_time
            if elapsed < min_search_interval:
                time.sleep(min_search_interval - elapsed)
            
            try:
                # Only search DuckDuckGo first (faster than arxiv)
                from langchain_community.tools import DuckDuckGoSearchRun
                from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
                wrapper = DuckDuckGoSearchAPIWrapper(backend="lite")
                ddg_search = DuckDuckGoSearchRun(api_wrapper=wrapper)
                search_result = ddg_search.run(query)
                last_search_time = time.time()
                search_cache[query] = (search_result, time.time())
            except Exception as search_error:
                # If search fails, just use LLM
                search_result = None
        
        # Combine with LLM for response
        if search_result and search_result.strip():
            prompt = f"Based on this search result, provide a helpful answer to: {query}\n\nSearch results:\n{search_result}"
        else:
            # No search result, just ask LLM
            prompt = query
        
        response = agent.invoke(prompt)
        return response.content if hasattr(response, 'content') else str(response)
        
    except Exception as e:
        return f"Agent error: {str(e)[:100]}"