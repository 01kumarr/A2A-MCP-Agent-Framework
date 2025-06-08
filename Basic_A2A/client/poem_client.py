import requests 
import json
import uuid

# step 1: Discover the server and base URL where the server agent is hosted 

base_url = "http://localhost:8000"

# use HTTP GET to fetch the agent card from the well-known discovery endpoint 
res = requests.get(f"{base_url}/.well-known/agent.json")

# check and if fails raise an error
if res.status_code != 200:
    raise Exception(f"Failed to fetch agent card and so Agent: {res.status_code} {res.text}")


agent_info = res.json() # parse the response json into a python dict 

print(f"Connected to agent: {agent_info['name']}-{agent_info['description']} at {base_url}")

# Generate a unique task id 
task_id = str(uuid.uuid4()) 

task_payload = {
    "id": task_id,
    "message": {
        "role": "user",
        "parts":[
            {
                "type": "text",
                "text": "Write a poem about the beauty of nature."  
            }
        ]
    }
} 

response = requests.post(f"{base_url}/tasks/send", json=task_payload)
if response.status_code != 200:
    raise Exception(f"Failed to send task: {response.status_code} {response.text}") 

response_data = response.json() 

messages = response_data.get("messages", []) 

if messages:
    final_reply = messages[-1].get("parts", [{}])[0].get("text", "")
    print(f"Agent's response: {final_reply}")
else:
    print("No messages received from the agent.")       


