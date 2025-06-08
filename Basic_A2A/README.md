# BasicA2A

This project demonstrates a simple A2A (Agent-to-Agent) interaction using **FastAPI** for the server agent and a Python client that sends tasks to the agent. The agent responds by generating a beautiful Shakespearean-style poem.

---

## Project Structure
Basic_A2A/
│
├── client/
│ └── poem_client.py # Client script to interact with the FastAPI agent server
│
└── server/
└── poem_server.py # FastAPI server implementing the poem-writing agent

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Install Dependencies

Run this command to install required packages:

```bash
pip install fastapi uvicorn requests

Start the Server From the server directory, run uvicorn poem_server:app --reload --host 0.0.0.0 --port 8000

In a separate terminal, from the client directory, run: python poem_client.py 

Description
The server exposes two endpoints:

/.well-known/agent.json — agent discovery endpoint providing metadata.

/tasks/send — receives tasks and returns a Shakespearean-style poem.

The client discovers the agent, sends a poem request task, and displays the agent’s reply.


Notes
Ensure the server is running before starting the client.

The poem is fixed in this example but can be extended or replaced in the server code.

License
This project is open source and free to use.

