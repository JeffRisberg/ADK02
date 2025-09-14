## ADK02
has a collection of agents, and a larger set of tools

based on https://google.github.io/adk-docs/tutorials/agent-team/

## Set up virtual environment

```
rm -rf .venv
virtualenv -p python3.12 .venv
. .venv/bin/activate
pip install --upgrade pip

pip install -r requirements.txt
```

## Usage

Update .env file with your API key

Then run the app with:

```bash
adk web
```

Then run the app at command line with:

```bash
adk run multi_tool_agent
```

Then run as server (go to localhost:8000/docs to see the API docs):

```
python server.py
```

# Close with deactivation of venv

```
deactivate
```
