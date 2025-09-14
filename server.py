import os
import uvicorn

from fastapi import FastAPI

from google.adk.cli.fast_api import get_fast_api_app
from google.adk.sessions import DatabaseSessionService

# Set up paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
AGENT_DIR = BASE_DIR  # Parent directory containing multi_tool_agent

# Set up DB path for sessions
session_service_uri = f"sqlite:///{os.path.join(BASE_DIR, 'sessions.db')}"
session_service = DatabaseSessionService(db_url=session_service_uri)

# Create the FastAPI app using ADK's helper
app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    session_service_uri=session_service_uri,
    allow_origins=["*"],  # In production, restrict this
    host="localhost",
    port=8000,
    reload_agents=True,
    web=True,  # Enable the ADK Web UI
)

# Add custom endpoints
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/agent-info")
async def agent_info():
    """Provide agent information"""
    from multi_tool_agent import root_agent
    return {
        "agent_name": root_agent.name,
        "description": root_agent.description,
        "model": root_agent.model,
        "tools": [t.__name__ for t in root_agent.tools]
    }

if __name__ == "__main__":
    print("Starting FastAPI server...")
    server = uvicorn.Server(uvicorn.Config(app))
    server.run()

